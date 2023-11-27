from django.contrib import admin
from django.urls import path,include
from Token_Authentication import views
from rest_framework.authtoken.views import obtain_auth_token
from Token_Authentication.auth import CustomAuthToken
 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("studentapi_b",views.StudentMVS,basename='stu_api_b')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include("rest_framework.urls",namespace='rest_api')),
    path('gettoken/',CustomAuthToken.as_view()),
]
