from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import *


class RegisterView(View):
    def get(self,request):
        return render(request,"page-user-register.html")
    def post(self,request):
        if request.POST.get("p1") != request.POST.get("p2"):
            return redirect("/registration/")
        u=User.objects.create_user(
            username=request.POST.get("email"),
            password=request.POST.get("p1")
        )
        m=Mijoz.objects.create(
            ism=request.POST['ism']+" "+request.POST.get("l"),
            email=request.POST['email'],
            jins=request.POST['gender'],
            user= u


        )
        Manzil.objects.create(
            shahar=request.POST['shahar'],
            davlat=request.POST['davlat'],
            mijoz=m


        )
        from django.core.mail import EmailMessage
        from django.conf import settings
        from django.template.loader import render_to_string
        t = render_to_string("salom.html", {"user": m})
        email = EmailMessage(
            "Alistyle do'koniga xush kelibsiz",
            t,
            settings.EMAIL_HOST_USER,
            [m.email],
        )
        email.fail_silently = False
        email.send()


        return redirect("/login/")


class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')
    def post(self,request):
        u=request.POST['email']
        p=request.POST['password']
        users=authenticate(request,username=u,password=p)
        if users is None:
            return redirect('/login/')
        else:
            login(request,users)
            return redirect("home")

class SettingView(View):
    def get(self,request):
        m=Mijoz.objects.get(user=request.user)
        manzil=Manzil.objects.get(mijoz=m)
        return render(request,"page-profile-setting.html",{"mijoz":m,'manzil':manzil})
    def post(self,request):
        if request.user.is_authenticated:
            if request.POST.get("forma")=="f1":
                m = Mijoz.objects.get(user=request.user)
                manzil = Manzil.objects.get(mijoz=m)
                m.ism=request.POST['ism']

                m.email=request.POST['email']
                m.tel=request.POST['tel']
                m.save()



                manzil.davlat=request.POST["davlati"]
                manzil.shahar=request.POST['shahar']
                manzil.zipcode=request.POST["zipcode"]
                manzil.save()
                return redirect("/setting/")

            if request.POST.get("forma")=="f2":
                m = Mijoz.objects.get(user=request.user)
                m.rasm = request.FILES.get("rasm")
                return redirect("/setting/")

        else:
            return redirect("home")



