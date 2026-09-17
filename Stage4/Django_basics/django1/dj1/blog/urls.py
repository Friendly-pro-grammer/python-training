from . import views
from django.urls import path

urlpatterns = [
    # path('admin/',admin.site.urls),
    path("",views.Home,name="home"),
    path("about/",views.About,name="About") 
]