from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .paginations import MyPageNumberPagination,MyLOP

# Create your views here.

# class MyPageNumberPagination(PageNumberPagination):
#     page_size=5


# CRUD using ModelViewSet
class StudentMVS(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # pagination_class=MyPageNumberPagination
    pagination_class=MyLOP






