from django.db import models
class studadm(models.Model):
    fname=models.TextField(max_length=50)
    lname=models.TextField(max_length=50)
    email=models.EmailField()
    standard=models.CharField(max_length=5)
    address=models.TextField(max_length=100)
    phone=models.IntegerField()
# Create your models here.
