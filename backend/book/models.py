# Python
import uuid

# Django
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    FileExtensionValidator
)

# Third party
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel
)

# Project
from core.models import Category
from backend.settings import MEDIA_ROOT


class Book(TimeStampedModel, TitleDescriptionModel):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    author = models.CharField(db_index=True)

    thumbnail = models.FileField(
        validators=[FileExtensionValidator(
            allowed_extensions=['png', 'jpg', 'jpeg'])],
        upload_to=MEDIA_ROOT)

    total_pages = models.IntegerField()

    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return f'{self.uid} - {self.title}'


class BookRating(TimeStampedModel):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        get_user_model(),
        related_name='book_rating',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    book = models.ForeignKey(
        Book,
        related_name='book_rating',
        on_delete=models.CASCADE
    )

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0,
        db_index=True)

    comment = models.TextField(max_length=450, blank=True, null=True)

    def __str__(self):
        if self.user:
            return f'{self.user.username} - {self.book.title}'
        return self.book.title

    @receiver(post_save, sender=Book)
    def register_book_rating(sender, instance, created, **kwargs):
        if created:
            BookRating.objects.create(book=instance)
