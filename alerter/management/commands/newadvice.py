from django.core.management.base import BaseCommand
from django.db.models import F
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string

import logging

from alerter.models import TradeAlert
from aim.models import Holding
from users.models import User

import time

logger = logging.getLogger(__name__)


def do_alerts():
    logger.info("Do alerts()")

    alert_set = []

    # loop over all users and see if any of them have alerts, if so, pass the whole user portfolio list to them and be done with it.
    for u in User.objects.all():

        alert_set = []

        # trigger determines if we break out of the lower loop for this user, if any of their holdings has an alert, them break out and run a report
        # for them.
        
        trigger = False

        logger.debug("checking %s" % u)        
        
        for p in u.portfolio_set.all().order_by("name"):
            logger.debug("Checking %s" % p)
            
            for h in p.holding_set.all().order_by("symbol__name"):

                logger.debug("Checking %s" % h)
                
                if h.alert():
                    alert_set.append(h)

        if alert_set:
            ctx = {"alert_set" : alert_set }
            message = render_to_string("alerter/email_report.html",ctx)
            mfrom = settings.EMAIL_HOST_USER
            send_mail(subject="Subject", message=None, html_message=message, from_email=mfrom, recipient_list=[u.email,])
                
#                u.email_user("subject", message, mfrom)

class Command(BaseCommand):
    args = None
    help = "Generates and emails all stock alerts"
    
    def handle(self, *args, **options):
        do_alerts()