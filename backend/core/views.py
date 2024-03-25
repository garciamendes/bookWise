# Third party
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

# Local
from .serializers import CategoriesListSerializer
from .models import Category

class CatagoryViewset(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer
    lookup_field = ['slug']
