from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router  =DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')
router.register('blogs',views.BlogsViewSet,basename="blogs")
router.register('comments',views.CommentsViewSet,basename="comments")
urlpatterns =[
    path('students',views.students_view,name="students-view"),
    path('students/<int:pk>',views.student_detail_view,name="student-detail-view"),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>',views.EmployeeDetail.as_view())
    
    path('',include(router.urls))  ,
    # path('blogs/',BlogsView.as_view()),
    # path('comments/',CommentsView.as_view())
]
