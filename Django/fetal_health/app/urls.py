from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexView,name="index"),
    #path("fileupload/",views.FileUpload,name="fileupload"),
    path("predict/",views.Prediction,name="predict"),
    path("home/",views.HomePage,name="home"),
    #path("about/",views.AboutPage,name="about"),
    path("login/",views.LoginUser,name="login"),
    path("logout/",views.LogOut,name="logout"),
    path("signin/",views.LoginPage,name="loginpage"),
    path("signup/",views.SignUpPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otp/",views.Otpverify,name="otp"),
    path("reset/",views.ResetPassword,name="reset"),
    
]