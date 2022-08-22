
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('home/logout',views.logout,name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('otp/',views.otp,name='otp'),
    path('<email>/change_password/',views.change,name='change_password'),
]
