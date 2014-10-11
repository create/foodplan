from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    page_info = {"page_title": "Home"}
    return render(request, 'home.html', {"page_info": page_info})


def signin(request):
    page_info = {"page_title": "Sign in"}
    return render(request, 'signin.html', {"page_info": page_info})


def signup(request):
    page_info = {"page_title": "Sign up"}
    return render(request, 'signup.html', {"page_info": page_info})


def pantry(request):
    page_info = {"page_title": "Your pantry"}
    return render(request, 'pantry.html', {"page_info": page_info})


def improve(request):
    page_info = {"page_title": "Improve"}
    return render(request, 'improve.html', {"page_info": page_info})


def dashboard(request):
    page_info = {"page_title": "Dashboard"}
    return render(request, 'dashboard.html', {"page_info": page_info})