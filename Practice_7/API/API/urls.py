from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter
from JWT import views

router=DefaultRouter()
router.register("stu_api",views.StudentMVS,basename='stu_api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh_view"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
    path('',include(router.urls)),
]


#   http POST http://127.0.0.1:8000/gettoken/ username="admin" password="123"
#   http POST http://127.0.0.1:8000/verifytoken/ token=" "
#   http POST http://127.0.0.1:8000/refreshtoken/ refresh=" "


#    http http://127.0.0.1:8000/stu_api/ "Authorization:Bearer "  