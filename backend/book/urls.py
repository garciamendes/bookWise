# Django
from django.urls import path
from django.urls import include

# Third party
from rest_framework.routers import DefaultRouter

# Local
from .views import BookViewset

router = DefaultRouter(trailing_slash=True)
router.register(r'', BookViewset)

urlpatterns = router.urls
