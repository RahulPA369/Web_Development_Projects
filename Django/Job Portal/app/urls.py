from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("verify/",views.OTPPage,name="otpverify"),
    path("otp/",views.Otpverify,name="otp"),
    path("login/",views.LoginPage,name="login"),
    path("loginpage/",views.LoginUser,name="loginpage"),
    path("model/",views.mlModel,name="model"),
]
