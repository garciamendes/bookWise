# Django
from django.contrib.auth import get_user_model

# Third party
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    total_page_read = serializers.IntegerField(
        source='profile.total_page_read')

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'total_page_read'
        ]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.total_page_read = profile_data.get(
            'total_page_read', profile.total_page_read)
        profile.save()

        return instance
