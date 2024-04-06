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
