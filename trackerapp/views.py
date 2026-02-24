from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# LOGIN (NO login_required here)
def employee_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "emplogin.html")


# DASHBOARD
@login_required
def home(request):
    return render(request, "home.html")


# CHECK IN
@login_required
def check_in(request):
    return render(request, "check_in.html")


# CHECK OUT
@login_required
def check_out(request):
    return render(request, "check_out.html")