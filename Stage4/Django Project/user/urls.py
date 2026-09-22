from django.urls import path
from . import views
urlpatterns = [
    path('role/create/',views.create_role,name="create-role")
]