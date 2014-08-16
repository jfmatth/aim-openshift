from django.db import models

# Create your models here.

from aim.models import Holding, HoldingAlert

# tradealert
# 
# Holds all email alerts that should go out to a user for each holding that is alerting.
class TradeAlert(models.Model):
    holding = models.ForeignKey(Holding)
    alert = models.OneToOneField(HoldingAlert,
                                 blank=True, null=True,
                                 on_delete=models.DO_NOTHING,
                                )
    
    date = models.DateField()  # when did alert get added
    emailed = models.BooleanField(default=False)  # was it emailed


## some testing i did
#
# get a list of all holdings that don't already have this alert, regardless of email status.
# hl = Holding.objects.exclude(currentalert=None).exclude(tradealert__alert=F("currentalert") )
# 
# add them as new alerts to the system via new TradeAlerts