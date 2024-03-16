# Python
import uuid

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel
)

# Project
from core.models import Catagory


class Book(TimeStampedModel, TitleDescriptionModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField()
    thumbnail = models.FileField(upload_to='upload')
    total_pages = models.IntegerField()
    categories = models.ManyToManyField(Catagory, related_name='books')


class BookRating(TimeStampedModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), related_name='book_rating', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_rating', on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField(max_length=450, blank=True, null=True)
