from django.db.models.signals import post_save
from django.dispatch import receiver 

from django.contrib.auth import get_user_model
from air_quality_app.apis.call_api import AirQuality

User = get_user_model()
       
@receiver(post_save, sender=User)
def handle_ledger_input(sender, instance: User, created, **kwargs):
    if created:
            ip_addr = instance.ip_address
            city = AirQuality.get_city(ip_addr)
            instance.air_city = city
            instance.save()