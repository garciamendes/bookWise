# Third party
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

# Local
from .serializers import CategoriesListSerializer
from .models import Catagory

class CatagoryViewset(ListModelMixin, GenericViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CategoriesListSerializer
