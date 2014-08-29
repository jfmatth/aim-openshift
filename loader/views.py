# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

import logging
import csv
import datetime
import StringIO

from aim.models import Symbol, Price
from loader.models import Exchange, ExchangePrice, PriceError
from loader.forms import LoaderForm

# Get an instance of a logger
logger = logging.getLogger(__name__)

@transaction.atomic
def ImportPrices(f):
    """
    Import a file f into the prices table.
    """
    dialect = csv.Sniffer().sniff( f.read(1024) )
    f.seek(0)
    reader = csv.reader(f, dialect)
        
    header = reader.next()

    if not header[0] == "Symbol" or not header[1] == "Date":
        raise Exception("Error - Header line in looks wrong, %s" % header)

    # add import improvement. 
    datecheck = None
    count = 0

    logger.info("Start importing prices file...")
    for csvline in reader:

        # skip the header.
        if csvline[0] == "Symbol":
            continue

        d = datetime.datetime.strptime(csvline[1], "%d-%b-%Y").date()

        if not datecheck == d:
            # this is the date we are checking, so load all symbols from price for 
            # this date and use it for quick checking.
            logger.debug("datecheck = %s" % d)
            datecheck = d
            symbollist = set(Price.objects.filter(date=d).values_list("symbol__name", flat=True))
            logger.debug("sybollist populated")

        # now use the symbollist to verify each CSV line w/o a lookup
        if csvline[0] in symbollist:
            # if we already have it here, then skip.
            logger.debug("skipping %s due to duplicate" % csvline[0])
            pass
        else:
            
            try:
                sym = Symbol.objects.get(name=csvline[0])
                p = Price()
                p.symbol = sym
                p.date = d
                p.high = csvline[3]
                p.low  = csvline[4]
                p.close = csvline[5]
                p.volume = csvline[6]
                p.save()
                
                count += 1
                
                # check if this price upload is 'newer' than the symbols current price
                if sym.currentprice == None or p.date > sym.currentprice.date:
                    sym.currentprice = p
                    sym.save()
    
            except ObjectDoesNotExist:
                logger.error("Problem with %s" % csvline)
                # add this to the price error if necessary
                p, c = PriceError.objects.get_or_create(symbolname = csvline[0] )
                
                
    logger.info("Finished loading %s prices" % count)


def LoadPrices(request):
    count = 0    
    for e in ExchangePrice.objects.filter(loaded=False):
        # we have an exchange that hasn't been loaded.
        
        # sniff it out and load it into Symbols.
        ImportPrices( StringIO.StringIO(e.data) )

        e.loaded = True
        e.save()
        count += 1

    return HttpResponse("Loaded %s Prices" % count)


@transaction.atomic
def ImportExchange(f):
    dialect = csv.Sniffer().sniff( f.read(1024) )
    f.seek(0)
    reader = csv.reader(f, dialect)
    
    header = reader.next()
    
    if not header[0] == "Symbol" or not header[1] == "Description":
        raise Exception("Error - Header line in %s looks wrong" % header)

    try:
        for csvline in reader:
            # assume all the records are here and the exceptions add them
            # 4/4/14 - JFM, Fix bug where Description changes
    #         Symbol.objects.get_or_create( name = csvline[0],description = csvline[1] )
            Symbol.objects.get_or_create( name = csvline[0],defaults = {"description": csvline[1]} )
    except:
        print "Error loading %s" % csvline
        
        
def LoadExchange(request):
    count = 0
    
    for e in Exchange.objects.filter(loaded=False):
        # we have an exchange that hasn't been loaded.
        
        # sniff it out and load it into Symbols.
        ImportExchange( StringIO.StringIO(e.data) )

        e.loaded = True
        e.save()
        
        count += 1

    return HttpResponse("%s Exchanges Loaded" % count)


@csrf_exempt
def FormExchange(request, exchange):

    # loads an Exchange via the RAW form via a POST

    if request.method == 'POST':
        
        form = LoaderForm(request.POST, request.FILES)

        if form.is_valid():
            # at this point request.FILES has the text we want, load it into a new Exchange record
            ex = Exchange.objects.get_or_create(name=exchange, data=request.FILES['exchangedata'].read() )
            ex.save()

            return HttpResponse("Exchange up-Loaded")
        else:
            return HttpResponse("Exchange NOT loaded")
    else:
        return HttpResponse("GET not supported")



def LoadAllExchange():
    logger.info("LoadAllExchange() starting...")

    n = 0
    
    #load any exchanges
    for e in Exchange.objects.filter(loaded=False):
        # we have an exchange that hasn't been loaded.
        
        # sniff it out and load it into Symbols.
        ImportExchange( StringIO.StringIO(e.data) )
        logger.debug("Exchange loaded.")

        e.loaded = True
        e.save()
        
        n += 1
    
    return n


def LoadAllPrices():
    logger.info("LoadAllPrices() starting...")

    n=0
    body = "Date\n"
    
    for e in ExchangePrice.objects.filter(loaded=False):
        # we have an exchange that hasn't been loaded.
        
        # sniff it out and load it into Symbols.
        ImportPrices( StringIO.StringIO(e.data) )
        body += str(e.exchange) + "-"+ e.data.splitlines()[1].split(",")[1] + "\n"
        e.loaded = True
        e.save()

        n += 1
        
    send_mail("SOTB: %s prices loaded" % n, body, "registration@compunique.com", ["john@compunique.com",], fail_silently=False)

    return n

def LoadAll(request):

    c1 = LoadAllExchange()
    c2 = LoadAllPrices()
    
#     #load any exchanges
#     for e in Exchange.objects.filter(loaded=False):
#         # we have an exchange that hasn't been loaded.
#         
#         # sniff it out and load it into Symbols.
#         ImportExchange( StringIO.StringIO(e.data) )
# 
#         e.loaded = True
#         e.save()
#         
#         c1 += 1
# 
#     c2 = 0    
#     for e in ExchangePrice.objects.filter(loaded=False):
#         # we have an exchange that hasn't been loaded.
#         
#         # sniff it out and load it into Symbols.
#         ImportPrices( StringIO.StringIO(e.data) )
# 
#         e.loaded = True
#         e.save()
#         c2 += 1

    return HttpResponse("%s Exchanges Loaded, %s Prices Loaded" % (c1,c2) )
    
    
@csrf_exempt
def ExchangeLoader(request, exchange):

    # loads an Exchange via the RAW form via a POST
    if request.method == 'POST':
        
        form = LoaderForm(request.POST, request.FILES)

        if form.is_valid():
            # at this point request.FILES has the text we want, load it into a new Exchange record
            ex, created = Exchange.objects.get_or_create(name=exchange, defaults={"loaded":False} )
            ex.loaded = False
            ex.data = request.FILES['formdata'].read()
            ex.save()
            
            return HttpResponse("Exchange up-Loaded")

        else:
            return HttpResponse("Exchange NOT loaded, for invalid")
    else:
        return HttpResponse("GET not supported")


@csrf_exempt
def PricesLoader(request, exchange):

    if request.method == 'POST':
        
        form = LoaderForm(request.POST, request.FILES)

        if form.is_valid():
            
            # find the exchange we are loading
            try:
                ex = Exchange.objects.get(name=exchange)
                p = ExchangePrice(exchange=ex, data=request.FILES['formdata'].read(), loaded=False )
                p.save()
                
                return HttpResponse("prices up-Loaded")
            except ObjectDoesNotExist:
                return HttpResponse("Exchange NOT found")

        else:
            return HttpResponse("Prices not loaded, form invalid")
    else:
        return HttpResponse("GET not supported")

