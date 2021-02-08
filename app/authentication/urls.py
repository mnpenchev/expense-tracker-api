from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (TokenRefreshView,)  # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>', PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name="password-reset-complete"),
]
