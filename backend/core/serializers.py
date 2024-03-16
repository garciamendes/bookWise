# Third party
from rest_framework import serializers

# Local
from .models import Catagory

class CategoriesListSerializer(serializers.Serializer):

    class Meta:
        model = Catagory
        fields = ['slug', 'title']
