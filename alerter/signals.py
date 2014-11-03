from users.signals import user_registered, user_activated
from django.dispatch import receiver
from django.core.mail import mail_admins

@receiver(user_registered)
def registered_callback(sender, **kwargs):
    mail_admins("User Registration", kwargs['user'])


@receiver(user_activated)
def activated_callback(sender, **kwargs):
    mail_admins("User Activated", kwargs['user'])

