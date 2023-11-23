from django.contrib import admin
from django.urls import path
from CB_API import views as cb_views
from Generic_API import views as generic_views
from Concrete_API import views as concrete_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', cb_views.StudentAPI.as_view()), 
    path('stu_api/<int:pk>', cb_views.StudentAPI.as_view()), 

    # Generic API
    path('studentapi/', generic_views.StudentList.as_view()),
    path('studentapi_g/', generic_views.StudentCreate.as_view()),
    path('studentapi_g/<int:pk>/', generic_views.StudentRetrive.as_view()),
    path('studentapi_g_update/<int:pk>/', generic_views.StudentUpdate.as_view()),
    path('studentapi_g_delete/<int:pk>/', generic_views.StudentDelete.as_view()),
    
    # Mixing Multiple options 
    path('lc_student/', generic_views.Student_LC.as_view()),
    path('rud_student/<int:pk>/', generic_views.RUDStudent.as_view()),

    # Concrete API
    path('c_stu_lc/', concrete_views.Stu_LC.as_view()),
    path('c_stu_rud/<int:pk>', concrete_views.Stu_RUD.as_view()),

]
