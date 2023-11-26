from django.contrib import admin
from django.urls import path,include
from Auth import views
from Session_auth import views as SA
from Custome_permission import views as CP
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("studentapi_b",views.StudentMVS,basename='stu_api_b')
router.register("studentapi_s",SA.StudentAPI,basename='stu_api_s')
router.register("studentapi_c",CP.StudentAPI,basename='stu_api_c')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include("rest_framework.urls",namespace='rest_api'))
]
