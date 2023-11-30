from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Pagination import views

router=DefaultRouter()
router.register("stu_api",views.StudentMVS,basename='stu_api')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include("rest_framework.urls",namespace='rest_api')),
]
