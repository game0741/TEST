from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import School, Classroom, Teacher, Student
from .serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            num_classrooms=models.Count('classrooms', distinct=True),
            num_teachers=models.Count('classrooms__teachers', distinct=True),
            num_students=models.Count('classrooms__students', distinct=True)
        )
        return queryset

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school']

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['school', 'classrooms', 'firstname', 'lastname', 'gender']
    search_fields = ['firstname', 'lastname']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']
    search_fields = ['firstname', 'lastname']
