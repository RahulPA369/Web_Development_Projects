from django.shortcuts import render,redirect
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

    return redirect('showpage')#name of url in urls.py

def ShowPage(request):
    all_data=Teacher.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

def EditPage(request,pk):
    get_data=Teacher.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata=Teacher.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    udata.save()
    return redirect('showpage')

def Delete(request,pk):
    ddate=Teacher.objects.get(id=pk)
    ddate.delete()
    return redirect('showpage')