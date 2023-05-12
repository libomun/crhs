from django.db.models.signals import post_save
from django.dispatch import receiver
from ..administration.models import User
from .models import Members

# when user sign up, member also was created


@receiver(post_save, sender=User)
def post_save_create_member(sender, instance, created, **kwargs):
    if created:
        Members.objects.create(user=instance)

