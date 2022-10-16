from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp =models.IntegerField()
    is_verified = models.BooleanField(default=False)

class Patient(models.Model):
    doc_id = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
