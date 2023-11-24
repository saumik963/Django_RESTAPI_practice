from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

# Create your views here.

# CRUD using ModelViewSet
class StudentMVS(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# ReadOnly Using ModelViewSet
class StudentROMVS(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer