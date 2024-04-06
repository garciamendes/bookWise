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
    categories = CategoriesListSerializer(many=True)
    rating = serializers.SerializerMethodField(method_name='get_rating')

    class Meta:
        model = Book
        fields = [
            'uid',
            'title',
            'description',
            'author',
            'thumbnail',
            'total_pages',
            'categories',
            'rating',
            'created',
        ]

    def get_rating(self, obj):
        book_rating = obj.book_rating.first()
        return book_rating.rating if book_rating else 0


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
