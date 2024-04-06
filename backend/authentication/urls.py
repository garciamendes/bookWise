# Django
from django.urls import (
    path,
    re_path
)

# Third part
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.urls import (
    LoginView,
    LogoutView,
    UserDetailsView,
)
from dj_rest_auth.registration.views import (
    VerifyEmailView,
    RegisterView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('register/', RegisterView.as_view(), name='rest_create_user'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
            name='account_confirm_email'),

    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('current-user/', UserDetailsView.as_view(), name='rest_user_details'),
]

if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
