from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.accounts.models import Profile


@receiver(post_save, sender=Profile)
def user_post_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
