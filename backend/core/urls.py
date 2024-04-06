# Django
from django.urls import (
    path,
    include
)

# Third party
from rest_framework.routers import DefaultRouter

# Local
from .views import CatagoryViewset

router = DefaultRouter(trailing_slash=True)
router.register(r'', CatagoryViewset, basename='categories')

urlpatterns = router.urls
