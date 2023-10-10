from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def student_info(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# function based

def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu, many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# Class based
class StudentListView(APIView):
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

