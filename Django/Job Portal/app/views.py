from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.http import HttpResponse
import joblib
# Create your views here.


def mlModel(request):
    model=joblib.load('app/ml/ml_fetal_health_model.joblib')
    pred=model.predict([[100,0,0,0,0,0,0]])
    val = ""
    if pred[0]==1.0:
        val = 'Normal'
    elif pred[0]==2.0:
        val='Suspect'
    else:
        val='Pathological'
    return HttpResponse(val)
    
        

def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def OTPPage(request):
    return render(request,"app/otpverify.html")

def LoginPage(request):
    return render(request,"app/login.html")

def RegisterUser(request):
    role=request.POST['role']
    if role == "Candidate":
        
        fname= request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcandidate = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname,)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password doesnot match"
                return redirect('login',{'msg':message})
                
    
    elif role == "Company":
        
        fname= request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcompany = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname,)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password doesnot match"
                return render(request,"app/signup.html",{'msg':message})
    else:
        message = "Select Role"
        return render(request,"app/signup.html",{'msg':message}) 

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message ="OTP verification Successfull"
            return render(request,"app/login.html",{'msg':message})
        else:
            message ="OTP is incorrect"
            return render(request,"app/otpverify.html",{'msg':message,'email':email})

    else:
        return render(request,"app/signup.html")

def LoginUser(request):
    if request.POST['role']=="Candidate":
        email=request.POST['email']
        password=request.POST['password']
        
        user=UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                request.session['type']=False
                return redirect('index')
            else:
                message ="Password Incorrect"
                return render(request,"app/login.html",{'msg':message})

        else:
            message ="User doesnot exist"
            return render(request,"app/login.html",{'msg':message})  
               


