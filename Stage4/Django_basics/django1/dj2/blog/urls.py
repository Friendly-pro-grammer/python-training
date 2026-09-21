from . import views
from django.urls import path,re_path

urlpatterns = [
    # path('admin/',admin.site.urls),
    path("",views.Home,name="home"),
    path("about/",views.About,name="About") ,
    path('post/<int:post_id>/"',views.post_details,name="post-details"),
    path('user/<str:username>',views.user_profile,name='user-profile'),
    # re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year),
    path('article/<int:year>/<int:month>',views.article_by_year,name="article-by-year "),
]