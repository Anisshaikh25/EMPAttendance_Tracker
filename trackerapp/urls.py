from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns=[
    
    path('',views.employee_login,name='emplogin'),
    path('dashboard/',views.home,name='home'),
]