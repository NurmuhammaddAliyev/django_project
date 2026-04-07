from django.urls import path

from .views import (
    admin_panel,
    assignment_detail,
    create_admin,
    home,
    lesson_detail,
    logout_view,
    student_panel,
    submission_detail,
    teacher_panel,
)

urlpatterns = [
    path("", home, name="home"),
    path("create-admin/", create_admin, name="create-admin"),
    path("logout/", logout_view, name="logout"),
    path("admin-panel/", admin_panel, name="admin-panel"),
    path("teacher-panel/", teacher_panel, name="teacher-panel"),
    path("student-panel/", student_panel, name="student-panel"),
    path("lesson/<int:pk>/", lesson_detail, name="lesson-detail"),
    path("assignment/<int:pk>/", assignment_detail, name="assignment-detail"),
    path("submission/<int:pk>/", submission_detail, name="submission-detail"),
]
