# Third party
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action

# Local
from .serializers import CategoriesListSerializer
from .models import Category


class CatagoryViewset(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer
    pagination_class = None

    @action(detail=False, methods=['get'], url_path='categories-filters')
    def categories_filters(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
