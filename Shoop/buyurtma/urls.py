from django.contrib import admin
from django.urls import path
from buyurtma.views import SavatView,BuyurtmaView,TanlanganView,TolovView,SavatqoshView,SavatochirView,TanlanganQoshView


urlpatterns = [



    path("savat/", SavatView.as_view()),
    path("tanlangan/",TanlanganView.as_view()),
    path("tanlangan-qosh/<int:pk>/", TanlanganQoshView.as_view()),
    path("",BuyurtmaView.as_view()),
    path("tolov/",TolovView.as_view()),
    path("savatqosh/<int:pk>/",SavatqoshView.as_view()),
    path("savat/ochir/<int:pk>/", SavatochirView.as_view()),

    ]

