from django.contrib import admin
from django.urls import path,include
from ViewSet import views as VS
from ModelViewSet import views as MVS
from rest_framework.routers import DefaultRouter

# Creating Router object

router= DefaultRouter()

# Register Student ViewSet With Router
router.register('studentapi_VS',VS.StudentViewSet,basename='student_vs')
router.register('studentapi_MVS',MVS.StudentMVS,basename='student_mvs')
router.register('studentapi_ROMVS',MVS.StudentROMVS,basename='student_romvs')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
