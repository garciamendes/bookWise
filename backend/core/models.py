# Python
import uuid

# Django
from django.db import models

# Third party
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel
)


class Category(TimeStampedModel, TitleSlugDescriptionModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
