from django.contrib import admin
from django.urls import path
from mainapp.views import IndexView,BolimView,IchkiView,Home2,MahsulotlarView,MahsulotView


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', IndexView.as_view(),name="home"),
    path('bolim/', BolimView.as_view(), name="bolim"),
    path("ichki/<int:pk>/", IchkiView.as_view(),name="ichki"),
    path("mahsulotlar/<int:pk>/",MahsulotlarView.as_view(),name="mahsulotlar"),
    path("mahsulot/<int:pk>/",MahsulotView.as_view(),name="mahsulot"),



]