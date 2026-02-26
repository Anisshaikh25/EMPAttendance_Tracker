from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns=[
    
    path('',views.employee_login,name='login'),
    path('dashboard/',views.home,name='dashboard'),
    path('check_in/',views.check_in,name='check_in'),
    path('check_out/',views.check_out,name='check_out'),
]