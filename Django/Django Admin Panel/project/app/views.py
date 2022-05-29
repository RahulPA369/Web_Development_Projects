from django.shortcuts import render
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request, "app/insert.html")

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = Teacher.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    return render(request, "app/show.html")
    