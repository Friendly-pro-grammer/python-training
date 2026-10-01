from django.urls import path
from .views import RegisterView,LoginView,ProfileView,SessionProfileView,LogoutView,TokenProfileView,TokenLogoutView,JWTProfileView
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('session/',SessionProfileView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('token/',auth_views.obtain_auth_token,name="token"),
    path('profile-token',TokenProfileView.as_view(),name="profile-view"),
    path('token-logout',TokenLogoutView.as_view(),name="token-logout"),
    path("jwt/",TokenObtainPairView.as_view(),name="jwt-obtain"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="jwt-refresh"),
    path("profile-jwt/",JWTProfileView.as_view(),name="profile-jwt"),
]