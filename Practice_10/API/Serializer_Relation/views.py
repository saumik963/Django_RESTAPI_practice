from django.shortcuts import render
from .serializer import SingerSerializer,SongSerializer
from .models import Singer,Song
from rest_framework import viewsets
# Create your views here.


class SingerVS(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongVS(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer



