# Third party
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Local
from .models import Book
from .filters import BookFilters
from .serializers import BookListSerializer


class BookViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filterset_class = BookFilters
    search_fields = ['author', 'title']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.get_queryset().prefetch_related('categories'))

        context_categories = {}
        for book in queryset:
            context_categories.setdefault(book.uid, [])
            for category in book.categories.all():
                context_categories[book.uid].append({
                    'name': category.title,
                    'slug': category.slug
                })

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context=context_categories)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context=context_categories)
        return Response(serializer.data)
