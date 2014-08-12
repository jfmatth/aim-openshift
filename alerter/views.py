from django.shortcuts import render
from django.db.models import F
from django.core.mail import send_mail

from alerter.models import TradeAlert
from aim.models import Holding

import time

def generate_alerts():
    # scans through the environment and generates any stock alerts that are needed.
    
    ALERT_DESC = "%s.\nCurrent Price %s.\nCurrent Buy Amount %s.\nCurrent Sell Amount %s\n"
    
    # our starting list ( needs to be optimized).  Only pick holdings that aren't already alerted for
    # emailed or not.
    alertlist = Holding.objects.exclude(currentalert=None).exclude(tradealert__alert=F("currentalert") )
    
    for h in alertlist:
        # see if these
        if h.alert():
            # this holding has an alert that hasn't been emailed before
            ta = TradeAlert()
            ta.holding = h
            ta.alert = h.currentalert
            ta.date = time.strftime("%Y-%m-%d")
            ta.description = ALERT_DESC % (h.currentalert, 
                                           h.symbol.currentprice, 
                                           h.controller.BuyAmount(), 
                                           h.controller.SellAmount()
                                        )
            ta.save()


def email_alerts():
    for e in TradeAlert.objects.filter(emailed=False):
        subj  = "Trade Alert for %s" % e.holding
        mess  = e.description
        mfrom = "john@compunique.com"
        mto   = [e.holding.portfolio.owner.email]
         
        send_mail(subj, mess, mfrom, mto, fail_silently=False)
        e.emailed = True
        e.save()