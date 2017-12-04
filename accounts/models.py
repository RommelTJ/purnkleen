from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy


class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        return self.get_queryset().all()


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')  # user.profile
    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail", kwargs={"username": self.user.username})


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)
