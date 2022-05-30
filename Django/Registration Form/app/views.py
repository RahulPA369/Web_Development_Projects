from django.shortcuts import render
from .models import * 

# Create your views here.
def RegisterView(request):
    return render(request,"app/register.html")

def RegisterUser(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user=User.objects.filter(Email=email)

        if user:
            message="User already exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message="User registered successfully"
                return render(request, "app/login.html",{'msg':message})
            else:
                message="Password doesnot match"
                return render(request,"app/register.html",{'msg':message})


def LoginView(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']

        try:
            user = User.objects.get(Email=email)
        except:
            message="User doesnot exist"
            return render(request, "app/register.html",{'msg':message})

        if user:
            if user.Password == password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request, "app/home.html")
            else:
                message="Password doesnot match"

        #else:       either use exception or use filter instead of get
        # message="User doesnot exist"
        # return render(request, "app/register.html",{'msg':message})
        

