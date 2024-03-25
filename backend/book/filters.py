# Third party
from django_filters import FilterSet
from django_filters import CharFilter

# Local
from .models import Book

class BookFilters(FilterSet):
    categories = CharFilter(method='categories_filter')

    class Meta:
        model = Book
        fields = ['categories']

    def categories_filter(self, queryset, name, values):
        if not values:
            return queryset

        categories_to_filters = values.split(',')
        return queryset.filter(categories__slug__in=categories_to_filters)
