from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def week(request):
    return render(request, 'week.html')


def pantry(request):
    return render(request, 'pantry.html')


def improve(request):
    return render(request, 'improve.html')


def dashboard(request):
    page_info = {"page_title": "Dashboard"}
    return render(request, 'dashboard.html', {"page_info": page_info})