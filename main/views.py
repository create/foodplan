from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    page_info = {"page_title": "Homepage"}
    return render(request, 'home.html', {"page_info": page_info})


def signin(request):
    page_info = {"page_title": "Sign In"}
    return render(request, 'signin.html', {"page_info": page_info})

def signup(request):
    page_info = {"page_title": "Sign Up"}
    return render(request, 'signup.html', {"page_info": page_info})
