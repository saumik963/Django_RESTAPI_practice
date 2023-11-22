from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.

class StudentList(GenericAPIView,ListModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)


class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    

# Mix List and Create

class Student_LC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


# Mix Retrive, Update and Delete

class RUDStudent(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)