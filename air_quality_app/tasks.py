from datetime import datetime

from celery import shared_task
from django.contrib.auth import get_user_model

from air_quality_app.apis.call_api import AirQuality

User = get_user_model()


@shared_task
def update_users_city(

):
    all_users = User.objects.all().filter(is_active=True) 
    if all_users:
        for user in all_users:
            city = AirQuality.get_city(user.ip_address)
            user.air_city = city
            user.save()

    return f"UPDATED USERS CITIES {datetime.now()}"