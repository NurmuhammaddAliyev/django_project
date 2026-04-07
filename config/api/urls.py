from django.urls import path

from .views import *

urlpatterns = [
    path("student/", get_student, name="get_student"),
    path("student/<int:pk>/", student_detail, name="student_detail"),
    path('create_student/', create_student, name="create_student"),
    path('update_student/<int:pk>/', update_student, name="update_student"),
    path('delete_student/<int:pk>/', delete_student, name="delete_student"),
    path("teacher/", get_teacher, name="get_teacher"),
    path("teacher/<int:pk>/", teacher_detail, name="teacher_detail"),
    path('create_teacher/', create_teacher, name="create_teacher"),
    path('update_teacher/<int:pk>/', update_teacher, name="update_teacher"),
    path('delete_teacher/<int:pk>/', delete_teacher, name="delete_teacher"),
]

