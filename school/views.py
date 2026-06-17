from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Student, Subject, Grade
from .serializers import (
    StudentSerializer,
    SubjectSerializer,
    GradeSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.order_by('id')
    serializer_class = StudentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_fields = ['email']
    search_fields = ['name', 'email']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.order_by('id')
    serializer_class = SubjectSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    search_fields = ['name']


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.order_by('id')
    serializer_class = GradeSerializer

    filterset_fields = ['student', 'subject']

# Create your views here.
