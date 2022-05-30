from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def ImagePage(request):
    return render(request,"app/image.html")

def UploadImage(request):
    if request.method=="POST":
        imgname = request.POST['imgname']
        pics=request.FILES['image']

        newimg=ImageUpload.objects.create(Imagename=imgname,Image=pics)
        return redirect('show')

def ImageFetch(request):
    all_img = ImageUpload.objects.all()
    return render(request,"app/show.html",{'key1':all_img})