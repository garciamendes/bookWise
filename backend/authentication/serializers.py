# Django
from django.contrib.auth import get_user_model

# Third party
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class CreateUserSerializer(SimpleUserSerializer):

    class Meta(SimpleUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name']


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']


class UserProfileListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='profile.created', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'created_at']
        read_only_fields = ('id', 'username', 'created_at')


class UserProfileCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()


class UserProfileUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
