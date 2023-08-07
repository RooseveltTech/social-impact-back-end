from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from air_quality_app.models import Comment, Forum


User = get_user_model()


@receiver(post_save, sender=Forum)
def update_user_team(sender, instance, created, **kwargs):
    if created:
        instance.active = True
        instance.save()

@receiver(post_save, sender=Comment)
def update_user_team(sender, instance, created, **kwargs):
    if created:
        instance.active = True
        instance.save()