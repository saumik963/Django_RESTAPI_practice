from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from Throttling.throttling import CustomeRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
# Create your views here.

# CRUD using ModelViewSet
class StudentMVS(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # throttle_classes=[AnonRateThrottle,UserRateThrottle]
    throttle_classes=[AnonRateThrottle,CustomeRateThrottle]
    

# Throttling using different scope

class Stu_List(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'

class Stu_Create(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'



class Stu_Retrive(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'

