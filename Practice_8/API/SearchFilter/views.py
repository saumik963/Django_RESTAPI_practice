from django.shortcuts import render
from Filter.models import Student
from Filter.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

# Searching
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends=[SearchFilter]
#     search_fields=['city','^name']


# Ordering

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
   
