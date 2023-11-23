from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView, RetrieveAPIView,RetrieveDestroyAPIView

# Create your views here.

# Concrete API views  
# Inharite any of this using the same process

class Stu_LC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class Stu_RUD(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer