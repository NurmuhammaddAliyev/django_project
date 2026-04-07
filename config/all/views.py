from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Assignment, Course, Lesson, Student, Submission, Teacher


def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


def home(request):
    return HttpResponse(
        """
        <h1>Learning Platform</h1>
        <p>Minimal backend sahifalar.</p>
        <ul>
            <li><a href="/admin-panel/">Admin panel</a></li>
            <li><a href="/teacher-panel/">Teacher panel</a></li>
            <li><a href="/student-panel/">Student panel</a></li>
        </ul>
        """
    )


def create_admin(request):
    username = "admin"
    password = "admin12345"
    email = "admin@example.com"

    if User.objects.filter(username=username).exists():
        return HttpResponse("Admin already exists")

    User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
    )
    return HttpResponse("Superuser created")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
@user_passes_test(is_admin)
def admin_panel(request):
    return HttpResponse(
        f"""
        <h1>Admin Panel</h1>
        <ul>
            <li>Ustozlar soni: {Teacher.objects.count()}</li>
            <li>Studentlar soni: {Student.objects.count()}</li>
            <li>Kurslar soni: {Course.objects.count()}</li>
            <li>Darslar soni: {Lesson.objects.count()}</li>
            <li>Vazifalar soni: {Assignment.objects.count()}</li>
            <li>Topshiriqlar soni: {Submission.objects.count()}</li>
        </ul>
        """
    )


@login_required
def teacher_panel(request):
    teacher = Teacher.objects.filter(user=request.user).first()
    if not teacher:
        return HttpResponse("Sizga teacher profile biriktirilmagan.", status=404)

    courses = teacher.courses.all()
    assignments = teacher.assignments.all()
    submissions = Submission.objects.filter(assignment__teacher=teacher)

    course_items = "".join(f"<li>{course.title}</li>" for course in courses) or "<li>Kurs yo'q</li>"
    assignment_items = "".join(
        f'<li><a href="/assignment/{assignment.id}/">{assignment.title}</a></li>'
        for assignment in assignments
    ) or "<li>Vazifa yo'q</li>"
    submission_items = "".join(
        f"<li>{submission.student.name} - {submission.assignment.title} - {submission.score_percent}%</li>"
        for submission in submissions
    ) or "<li>Topshiriq yo'q</li>"

    return HttpResponse(
        f"""
        <h1>Teacher Panel</h1>
        <p>Ustoz: {teacher.name}</p>
        <h2>Kurslar</h2>
        <ul>{course_items}</ul>
        <h2>Vazifalar</h2>
        <ul>{assignment_items}</ul>
        <h2>Natijalar</h2>
        <ul>{submission_items}</ul>
        """
    )


@login_required
def student_panel(request):
    student = Student.objects.filter(email=request.user.email).first()
    if not student:
        return HttpResponse("Sizga student profile biriktirilmagan.", status=404)

    courses = student.courses.all()
    lessons = Lesson.objects.filter(course__in=courses)
    assignments = Assignment.objects.filter(course__in=courses)
    submissions = student.submissions.all()

    course_items = "".join(f"<li>{course.title}</li>" for course in courses) or "<li>Kurs yo'q</li>"
    lesson_items = "".join(
        f'<li><a href="/lesson/{lesson.id}/">{lesson.title}</a></li>'
        for lesson in lessons
    ) or "<li>Dars yo'q</li>"
    assignment_items = "".join(
        f'<li><a href="/assignment/{assignment.id}/">{assignment.title}</a></li>'
        for assignment in assignments
    ) or "<li>Vazifa yo'q</li>"
    submission_items = "".join(
        f'<li><a href="/submission/{submission.id}/">{submission.assignment.title}</a> - {submission.score_percent}%</li>'
        for submission in submissions
    ) or "<li>Topshirilgan ish yo'q</li>"

    return HttpResponse(
        f"""
        <h1>Student Panel</h1>
        <p>Student: {student.name}</p>
        <h2>Kurslar</h2>
        <ul>{course_items}</ul>
        <h2>Darslar</h2>
        <ul>{lesson_items}</ul>
        <h2>Vazifalar</h2>
        <ul>{assignment_items}</ul>
        <h2>Kod Editor</h2>
        <pre style="background:#111;color:#eee;padding:12px;border-radius:8px;">
def solution():
    return "Hello, world!"
        </pre>
        <h2>Natijalar</h2>
        <ul>{submission_items}</ul>
        """
    )


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return HttpResponse(
        f"""
        <h1>{lesson.title}</h1>
        <p>Kurs: {lesson.course.title}</p>
        <div>{lesson.content}</div>
        """
    )


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return HttpResponse(
        f"""
        <h1>{assignment.title}</h1>
        <p>Kurs: {assignment.course.title}</p>
        <p>Ustoz: {assignment.teacher.name}</p>
        <p>Til: {assignment.language}</p>
        <p>Deadline: {assignment.deadline or "Belgilanmagan"}</p>
        <h2>Tavsif</h2>
        <div>{assignment.description}</div>
        <h2>Starter Code</h2>
        <pre style="background:#111;color:#eee;padding:12px;border-radius:8px;">{assignment.starter_code or ""}</pre>
        """
    )


@login_required
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    result_items = "".join(
        f"<li>Test {result.test_case.id}: {'Passed' if result.passed else 'Failed'}</li>"
        for result in submission.results.all()
    ) or "<li>Natija yo'q</li>"

    return HttpResponse(
        f"""
        <h1>Submission Detail</h1>
        <p>Student: {submission.student.name}</p>
        <p>Vazifa: {submission.assignment.title}</p>
        <p>Foiz: {submission.score_percent}%</p>
        <p>Status: {submission.status}</p>
        <h2>Kod</h2>
        <pre style="background:#111;color:#eee;padding:12px;border-radius:8px;">{submission.code}</pre>
        <h2>Test Natijalari</h2>
        <ul>{result_items}</ul>
        """
    )
