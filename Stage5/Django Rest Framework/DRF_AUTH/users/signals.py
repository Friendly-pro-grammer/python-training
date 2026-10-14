from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.cache import cache

from .models import UserProfile
User = get_user_model()

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
@receiver(post_delete, sender=User)
def invalidate_user_count_cache(sender, **kwargs):
    cache.delete("users:count")
