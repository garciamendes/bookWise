# Third party
from django_filters.rest_framework import FilterSet

# Local
from .models import Book

class BookFilters(FilterSet):

    class Meta:
        model = Book
        fields = ['categories']
