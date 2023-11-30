from django.contrib import admin
from django.urls import path,include
from Throttling import views
from rest_framework.authtoken.views import obtain_auth_token

 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("studentapi_b",views.StudentMVS,basename='stu_api_b')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('list/',views.Stu_List.as_view()),
    path('create/',views.Stu_Create.as_view()),
    path('retrive/',views.Stu_Retrive.as_view()),


    path('auth/',include("rest_framework.urls",namespace='rest_api')),

]