from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from userapp.views import RegisterView,LoginView,SettingView
from buyurtma.views import LogoutView
from mainapp.views import Home2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',RegisterView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('home/',include("mainapp.urls")),
    path('buyurtma/',include("buyurtma.urls")),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('', Home2.as_view()),
    path("setting/",SettingView.as_view())



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
