from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.RegisterView,name="registerpage"),
   path("register/",views.RegisterUser,name="register"),
   path("login/",views.LoginView,name="loginpage"),
   path("loginuser/",views.LoginUser,name="login"),
   
]
