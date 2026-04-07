from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=150)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["order"]


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=150)
    description = models.TextField()
    starter_code = models.TextField(blank=True)
    language = models.CharField(max_length=50, default="python")
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"


class TestCase(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="test_cases")
    input_data = models.TextField()
    expected_output = models.TextField()
    is_hidden = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.assignment.title} - Test {self.id}"

    class Meta:
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"


class Submission(models.Model):
    PENDING = "pending"
    CHECKED = "checked"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (CHECKED, "Checked"),
    )

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="submissions")
    code = models.TextField()
    score_percent = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"


class SubmissionResult(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="results")
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name="results")
    passed = models.BooleanField(default=False)
    actual_output = models.TextField(blank=True)

    def __str__(self):
        return f"{self.submission} - {self.test_case}"

    class Meta:
        verbose_name = "Submission Result"
        verbose_name_plural = "Submission Results"


