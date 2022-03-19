from django.db import models
from userapp.models import Mijoz,Manzil
from mainapp.models import Mahsulot




class Savat(models.Model):
    mijoz=models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    son=models.PositiveSmallIntegerField(default=1)

class Buyurtma(models.Model):
    sana=models.DateTimeField(auto_now_add=True)
    summa=models.PositiveIntegerField()
    mijoz=models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    savat=models.ManyToManyField(Savat)

class Tanlangan(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    son=models.PositiveSmallIntegerField(default=1,blank=True,null=True)

class Tolov(models.Model):
    tezkor=models.BooleanField(default="False")
    manzil = models.ForeignKey(Manzil, on_delete=models.SET_NULL, null=True)
    karta_ism=models.CharField(max_length=30)
    raqam=models.CharField(max_length=17)
    cvv=models.CharField(max_length=3)
    oy=models.PositiveSmallIntegerField()
    yil=models.PositiveSmallIntegerField()
    buyurtma=models.OneToOneField(Buyurtma,on_delete=models.SET_NULL,null=True)



