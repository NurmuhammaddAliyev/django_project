from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from all.models import Student, Teacher

from .serializers import StudentSerializer, TeacherSerializer


@api_view(["GET"])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(["POST"])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return Response({"message": "Student o'chirildi"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_teacher(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data)


@api_view(["POST"])
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TeacherSerializer(teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    teacher.delete()
    return Response({"message": "Teacher o'chirildi"}, status=status.HTTP_200_OK)
