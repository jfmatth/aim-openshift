from django.core.management.base import BaseCommand
from django.db.models import F
from django.conf import settings

from django.template.loader import render_to_string

import logging

from alerter.models import TradeAlert
from aim.models import Holding

import time

logger = logging.getLogger(__name__)

def generate_alerts():

    logger.info("generate_alerts() - Start")    

    # our starting list ( needs to be optimized).  Only pick holdings that aren't already alerted for
    # emailed or not.
    alertlist = Holding.objects.exclude(currentalert=None).exclude(tradealert__alert=F("currentalert") )
    
    for h in alertlist:
        # see if these
        
        if h.alert():
            # this holding has an alert that hasn't been emailed before
            logger.debug("Alert found for %s" % h)
            ta = TradeAlert()
            ta.holding = h
            ta.alert = h.currentalert
            ta.date = time.strftime("%Y-%m-%d")
            ta.save()

    logger.info("generate_alerts() - End")    


def email_alerts():
    logger.info("email_alerts() - Start")
    
    for e in TradeAlert.objects.filter(emailed=False):
        ctx = {"alert" : e}
        
        subject  = render_to_string("alerter/email_subject.txt", ctx)
        subject = ''.join(subject.splitlines())

        message = render_to_string("alerter/email.txt",ctx)

        mfrom = settings.EMAIL_HOST_USER
         
        try:
            e.holding.portfolio.owner.email_user(subject, message, mfrom)
            e.emailed = True
            e.save()
            logger.debug("Emailed user %s" % subject)
            
        except:
            logger.exception("Error emailing alert to user") 

    logger.info("email_alerts() - End")
                                             

class Command(BaseCommand):
    args = None
    help = "Generates and emails all stock alerts"
    
    def handle(self, *args, **options):
        generate_alerts()
        email_alerts()
