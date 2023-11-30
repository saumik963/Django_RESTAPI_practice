from django.contrib import admin
from django.urls import path,include
from Filter import views as F
from SearchFilter import views as SF

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', F.Stu_List.as_view()),
    path('list_s/', SF.StudentList.as_view()),
    path('auth/',include("rest_framework.urls",namespace='rest_api')),

]
