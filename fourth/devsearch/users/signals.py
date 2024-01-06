from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User


def profile_updated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(profile_updated, sender=User)
post_delete.connect(delete_user, sender=Profile)
