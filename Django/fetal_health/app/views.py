from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import randint
from app.functions.function import handle_uploaded_file,rfPrediction 
from django.core.mail import EmailMessage
from threading import Thread

# Create your views here.


def IndexView(request):
    return render(request,"app/index.html")

def LoginPage(request):
    return render(request,"app/login.html")

def SignUpPage(request):
    return render(request,"app/signup.html")

def HomePage(request):
    if 'firstname' in request.session.keys():
        return render(request,"app/home.html")
    else:
        return redirect('loginpage')

def AboutPage(request):
    return render(request,"app/about.html")

def LogOut(request):
    request.session.flush()
    return redirect('index')

def mail_send(otp,email,flag):

    if flag:
        verEmail = EmailMessage(
                    f'Medi Care - Account Verification',
                    f'Your verification code is {otp}',
                    'Medi Care<qwertymail625@gmail.com>',
                    [email],
                    headers={'Message-ID': 'Medi Care'},
                    )
        verEmail.send(fail_silently=False)

    else:
        verEmail = EmailMessage(
                    f'Medi Care - Reset Password',
                    f'Your password reset code is {otp}',
                    'Medi Care<qwertymail625@gmail.com>',
                    [email],
                    headers={'Message-ID': 'Medi Care'},
                    )
        verEmail.send(fail_silently=False)

def RegisterUser(request):
    if request.method =="POST":     
        fname= request.POST['fname'].upper()
        lname =request.POST['lname'].upper()
        email =request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = Doctor.objects.filter(email=email)

        if user:
            message = "User Already Exist"
            return render(request,"app/login.html",{'msg':message,'email':email})
        else:
            if password==cpassword:
                otp = randint(100000, 999999)

                try:
                    Thread(target=mail_send, args=(otp,email,True, )).start()                  
                except:
                    message = "Error occured. Try after some time."
                    return render(request,"app/signup.html",{'msg':message})

                newuser = Doctor.objects.create(firstname=fname,lastname=lname,otp=otp,email=email,password=password)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password doesnot match"
                return render(request,"app/signup.html",{'msg':message,'email':email,'fname':fname,'lname':lname})
    else:
        return redirect('signup')
                
def Otpverify(request):
    if request.method =="POST":
        email = request.POST['email']
        otp = int(request.POST['otp'])

        user = Doctor.objects.get(email=email)

        if user:
            if user.otp == otp:
                user.is_verified=True
                user.save()
                message ="success"
                return HttpResponse(message)
            else:
                message ="Verification code is incorrect"
                return HttpResponse(message)

        else:
            return render(request,"app/signup.html")
    else:
        return redirect('loginpage')

def LoginUser(request):
    if request.method =="POST":
        email=request.POST['email']
        password=request.POST['password']
        
        try:
            user = Doctor.objects.get(email=email)
        except Doctor.DoesNotExist:
            user = None

        if user:
            if user.password==password:
                if user.is_verified==False:
                    message="Please verify your account"
                    return render(request,"app/otpverify.html",{'msg':message,'email':email})
                
                can = Doctor.objects.get(email=email)
                request.session['id']=user.id
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                request.session['type']=False
                return redirect('home')

            else:
                message ="Password Incorrect"
                return render(request,"app/login.html",{'msg':message,'email':email})

        else:
            message ="User doesnot exist"
            return render(request,"app/login.html",{'msg':message}) 
    else:
        return redirect('loginpage')

def FileUpload(request):
    if request.method =="POST":
        print(request.POST)
        fname=randint(100000, 999999)
        files=request.FILES['files']
        handle_uploaded_file(files,fname)
        with open(f'app/upload/{fname}.txt') as f:
            contents = f.read()
        pred = [[int(x) for x in contents.split(",")]]
        val=rfPrediction(pred) 
        return render(request,"app/result.html",{'pred':val})
    else:
        if 'firstname' in request.session.keys():
            return render(request,"app/result.html") 
        else:
            return redirect('loginpage')
        

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Prediction(request):
    if is_ajax(request=request) and request.method =="POST":
        bline=request.POST['bline']
        acc=request.POST['acc']
        fm=request.POST['fm']
        uc=request.POST['uc']
        ld=request.POST['ld']
        sd=request.POST['sd']
        pd=request.POST['pd']
        astv=request.POST['astv']
        val=rfPrediction([[bline,acc,fm,uc,ld,sd,pd,astv]])    
        return HttpResponse(val)
    else:
        return HttpResponse("Error") 

def ResetPassword(request):
    if 'email' in request.POST.keys():
        email =request.POST['email']
        try:
            user = Doctor.objects.get(email=email)
        except Doctor.DoesNotExist:
            user=None
        if user:
            try:
                otp = randint(100000, 999999)
                Thread(target=mail_send, args=(otp,email,False, )).start()
                user.otp=otp
                user.save()
            except:
                message = "Error occured. Try after some time."
                return HttpResponse(message) 
            message = "Code Sent"
            return HttpResponse(message) 
        else:
            message = "User doesnot exist"
            return HttpResponse(message)

    elif 'otp' in request.POST.keys():
        print(request.POST)
        otp = int(request.POST['otp'])
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        try:
            user = Doctor.objects.get(otp=otp)
        except Doctor.DoesNotExist:
            user=None

        if user:
            if password==cpassword:
                user.password=password
                user.save()
                message ="success"
                return HttpResponse(message)
            else:
                message = "Password doesnot match"
                return HttpResponse(message)
        else:    
            message ="Incorrect reset code"
            return HttpResponse(message)

    else:
        return render(request,"app/resetpass.html")
        