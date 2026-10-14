from django.urls import path,include
from .views import RegisterView,ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('accounts/',include("allauth.urls")),
    path("_allauth/",include("allauth.headless.urls"))
]