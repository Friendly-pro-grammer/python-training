from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.student_create,name='student-create'),
    path('get-all/',views.student_list,name='student-read'),
    path('student/<int:pk>/',views.student_detail,name="student-detail"),
    path('edit/<int:pk>',views.student_edit,name="student-edit"),
    path('delete/<int:pk>/',views.student_delete,name="student-delete")
]