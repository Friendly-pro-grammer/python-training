from django.urls import path
from . import views
urlpatterns =[
    path('students',views.students_view,name="students-view"),
    path('students/<int:pk>',views.student_detail_view,name="student-detail-view"),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>',views.EmployeeDetail.as_view())
]