# Python
import uuid

# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Third party
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel
)


class Profile(TimeStampedModel, ActivatorModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    total_page_read = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=get_user_model())
    def register_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
