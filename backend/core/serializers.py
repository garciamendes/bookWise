# Third party
from rest_framework import serializers

# Local
from .models import Category

class CategoriesListSerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ['slug', 'title']
