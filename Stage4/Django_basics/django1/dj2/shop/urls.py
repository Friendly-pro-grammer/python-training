from . import views
from django.urls import path

urlpatterns = [
    # path('admin/',admin.site.urls),
    path("",views.Home,name="shop-home"),
    path("product/",views.Products,name="shop-product") 
]