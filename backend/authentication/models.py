# Python
import uuid

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel
)


class Profile(TimeStampedModel, ActivatorModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    total_page_read = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username