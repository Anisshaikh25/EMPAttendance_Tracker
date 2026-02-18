from django.shortcuts import HttpResponse,render,redirect


def home(request):
    return HttpResponse('hello')

def emplogin(request):
    return render(request,'emplogin.html')