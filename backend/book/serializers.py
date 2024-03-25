# Third party
from rest_framework import serializers

# Project
from core.serializers import CategoriesListSerializer

# Local
from .models import (
    Book,
    BookRating
)


class BookListSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'uid',
            'author',
            'thumbnail',
            'total_pages',
            'categories',
            'created',
        ]

    def get_categories(self, obj):
        return self.context.get(obj.uid, [])


class BookCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'author',
            'thumbnail',
            'total_pages',
            'categories'
        ]


class BookRatingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = [
            'user',
            'rating',
            'comment'
        ]
