from django.contrib import admin

from .models import Course, Student, Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_at")
    search_fields = ("name", "user__username")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher")
    search_fields = ("title", "teacher__name")
    list_filter = ("teacher",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ("name", "email", "courses")
    list_display = ("name", "email", "get_courses")
    search_fields = ("name", "email")
    filter_horizontal = ("courses",)

    def get_courses(self, obj):
        return ", ".join(course.title for course in obj.courses.all())

    get_courses.short_description = "Courses"
