from django.contrib.auth.models import User
from django.db import models

class Mijoz(models.Model):
    ism=models.CharField(max_length=35)
    rasm=models.FileField(upload_to="mijoz",blank=True)
    email=models.EmailField()
    tel=models.CharField(max_length=30,blank=True)
    jins=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.ism

class Manzil(models.Model):
    shahar=models.CharField(max_length=25)
    davlat=models.CharField(max_length=35)
    kocha=models.CharField(max_length=40,blank=True)
    uy=models.CharField(max_length=40,blank=True)
    zipcode=models.PositiveIntegerField(blank=True,null=True)
    mijoz=models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.kocha},{self.uy}"












