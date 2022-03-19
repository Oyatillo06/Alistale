from django.shortcuts import render, redirect
from django.views import View

from .models import *


class IndexView(View):
    def get(self,request):
        if request.user.is_authenticated:
            b = Bolim.objects.all()
            return render(request,'page-index.html', {"bolimlar":b})
        else:
            return redirect("login")
class BolimView(View):
    def get(self, request):
        if request.user.is_authenticated:
            b = Bolim.objects.all()
            i = Ichki.objects.all()
            return render(request, "page-category.html", {"bolimlar": b, "ichkilar": i})
        else:
            return redirect("login")


class Home2(View):
    def get(self, request):
        b = Bolim.objects.all()
        return render(request, "page-index-2.html", {"bolimlar":b})
class IchkiView(View):
    def get(self, request,pk):
        if request.user.is_authenticated:
            b = Bolim.objects.get(id=pk)
            i =b.ichki_bolimlar.all()
            return render(request, "ichki.html", {"bolimlar": b, "ichkilar": i})
        else:
            return redirect("login")
class MahsulotlarView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            i=Ichki.objects.get(id=pk)
            m=i.mahsulotlar.all()
            return render(request,"page-listing-grid.html",{"mahsulotlar":m})
        else:
            return redirect("login")



class MahsulotView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            m=Mahsulot.objects.get(id=pk)
            return render(request,"page-detail-product.html",{"mahsulot":m})
        else:
            return redirect("login")