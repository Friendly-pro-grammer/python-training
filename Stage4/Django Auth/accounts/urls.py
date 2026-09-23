from django.urls import path
from . import views


urlpatterns =[
    path(
        "register/",
        views.register,
        name="register"
    ),
    path(
        "login/",
        views.login_user,
        name="login"
    ),
    path(
        "logout/",
        views.logout_user,
        name="logout"
    ),
    path(
        "profile/",
        views.profile,
        name="profile"
    ),
    path(
        'protected',
        views.protected_endpoint,
        name="protected"
    ),
    path(
    "csrf/",
    views.csrf_token,
    name="csrf-token"
        ),
    path(
        "manager-dashboard/",
        views.manager_dashboard,
        name="manager-dashboard"
    ),
    path(
        "admin-dashboard",
        views.admin_dashboard,
        name="admin-dashboard"
    )
]