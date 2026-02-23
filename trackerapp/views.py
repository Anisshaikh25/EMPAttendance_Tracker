from django.shortcuts import render,redirect

# Create your views here.



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def employee_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")   # after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "emplogin.html")


def home(request):
    return render(request, "home.html")