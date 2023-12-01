from django.contrib import admin
from django.urls import path,include
from Serializer_Relation import views
from rest_framework.routers import DefaultRouter

rout=DefaultRouter()

rout.register("singer",views.SingerVS,basename='singer')
rout.register("song",views.SongVS,basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(rout.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
