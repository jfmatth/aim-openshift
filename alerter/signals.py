from users.signals import user_registered, user_activated
from django.dispatch import receiver
from django.core.mail import mail_admins

import logging
logger = logging.getLogger(__name__)

@receiver(user_registered)
def registered_callback(sender, **kwargs):
    logger.info("User Registration %s" % kwargs['user'])
    
    mail_admins("User Registration %s"  % kwargs['user'], str(kwargs['request']) )


@receiver(user_activated)
def activated_callback(sender, **kwargs):
    logger.info("User Activated %s" % kwargs['user'])
    
    mail_admins("User Activated %s" % kwargs['user'], str(kwargs['request']))

