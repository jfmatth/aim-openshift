__author__ = 'jfmatth'

from optparse import make_option
import datetime

from django.core.management.base import BaseCommand
from loadprices import LoadAll

from aim.daterange import Daterange

import logging

logger = logging.getLogger(__name__)


# turn this into a management command.
class Command(BaseCommand):
    args = "Date optional"
    help = "loads all stock prices for <date>"

    option_list = BaseCommand.option_list + (
        make_option('--start',
                    default=False,
                    help='<date> = YYYY-mm-dd, Start date for historical prices load'),
    )

    def handle(self, *args, **options):
        # self.stdout.write("Loadprices.py - calling LoadAll()")
        # LoadAll()
        # self.stdout.write("Loadprices.py - Complete")

        sd = datetime.datetime.strptime(options['start'], "%Y-%m-%d").date()
        ed = datetime.date.today()

        for x in Daterange(sd, ed):
            print x

            if (datetime.date.today() - x).days > 7:
                h = True
            else:
                h = False

            LoadAll(date=x, history=h)
