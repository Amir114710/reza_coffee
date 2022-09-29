from django.urls import path , re_path , include
from . import views


app_name = 'account'


urlpatterns = [
    path('otp_registeration' , views.OtpRegisterationView.as_view() , name="otp"),
    path('check_otp' , views.CheckOtpCode.as_view() , name="check_otp"),
    path('logout' , views.logout_user , name="logout"),
]
