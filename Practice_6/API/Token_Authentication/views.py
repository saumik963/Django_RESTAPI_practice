from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Token_Authentication.custome_auth import CustomeAuthentication
# Create your views here.

# CRUD using ModelViewSet
class StudentMVS(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomeAuthentication]
    permission_classes=[IsAuthenticated]
    



# Command to create token ---> http POST http://127.0.0.1:8000/gettoken/ username="John" password="jhonpass"

#  http DELETE http://127.0.0.1:8000/studentapi_b/6/ "Authorization:Token 6c128eb820c6299f119bd7c26403031bbd26a26f"