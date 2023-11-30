from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# class Stu_List(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     def get_queryset(self):
#         user=self.request.user
#         return Student.objects.filter(passby=user)


class Stu_List(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['city','name']
