# Django
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Third party
from allauth.account.signals import email_confirmed
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

# Local
from .serializers import CurrentUserSerializer

# @receiver(email_confirmed)
# def email_confirmed_(request, email_address, **kwargs):
#     user = email_address.user
#     user.email_verified = True

#     user.save()


class CurrentUserViewset(RetrieveModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CurrentUserSerializer
