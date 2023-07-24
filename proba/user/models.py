from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver  
from .helpers import send_registration_confirmation_email
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

@receiver(post_save, sender=User) 
def create_product(sender, instance, created, **kwargs):
    if created:
        print("Save method is called")
        print(instance)
        
    else:
        print("Update method is called")
        print(instance)
        body = render_to_string('user/email_registration_confirmed.html', {'username':instance.username})
        email = EmailMessage(
        'Account registration complete',
        body,
        'admin@proba.com',
        [instance.email]
        )
        email.send()
