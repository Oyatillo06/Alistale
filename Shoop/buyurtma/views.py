from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Mijoz
from mainapp.models import Mahsulot

class SavatView(View):
    def get(self,request):
        if request.user.is_authenticated:
            m=Mijoz.objects.get(user=request.user)
            s=Savat.objects.filter(mijoz=m)
            t=Tanlangan.objects.filter(mijoz=m)
            umumiy=0
            for i in s:
                umumiy=umumiy+(i.son*i.mahsulot.narx)
            a=0
            for i in s:
                a=a+(i.son *((i.mahsulot.narx * i.mahsulot.aksiya)/100))
            return render(request,"page-shopping-cart.html",{"tanlangan":t,"savat":s,"umumiy":umumiy,"aksiya":a,"yakun":umumiy-a})
        else:
            return redirect("login")




class TanlanganView(View):
    def get(self,request):
        if request.user.is_authenticated:
            mijoz=Mijoz.objects.get(user=request.user)
            s=Tanlangan.objects.filter(mijoz=mijoz)
            return render(request,"page-profile-wishlist.html",{"tanlanganlar":s})
        else:
            return redirect("login")
class TanlanganQoshView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            m=Mijoz.objects.get(user=request.user)
            savat=Savat.objects.get(id=pk)
            mah=Mahsulot.objects.get(id=savat.mahsulot.id)
            Tanlangan.objects.create(
                mijoz=m,
                mahsulot=mah,
                son=savat.son


            )
            return redirect("/buyurtma/savat/")
        else:
            return redirect("login")




class BuyurtmaView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,"page-profile-orders.html")
        else:
            return redirect("login")

class TolovView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,"page-payment.html")
        else:
            return redirect("login")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")


class SavatqoshView(View):
    def get(self,request,pk):
        m=Mijoz.objects.get(user=request.user)
        mah=Mahsulot.objects.get(id=pk)
        savat=Savat.objects.filter(mijoz=m)
        for i in savat:
            if i.mahsulot == mah:
                return redirect("mahsulot",pk)

        Savat.objects.create(
            mijoz=m,
            mahsulot=mah,
            son=request.GET.get("soni")


        )
        return redirect("mahsulot",pk)

class SavatochirView(View):
    def get(self,request,pk):
        Savat.objects.get(id=pk).delete()
        return redirect("/buyurtma/savat/")