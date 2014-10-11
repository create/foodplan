import json
from django.shortcuts import render
from django.http import HttpResponse
import requests
from models import Recipe

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

def get_recipe(request):
    app_id = "e91111f8"
    app_key = "f9d16213fe4a2371bb8c919c89dc409a"

    # specify random healthy ingredients to get enough data out of the API
    #terms = ["carrot", "onion", "potato", "tomato", "cucumber"]
    terms = ["carrot"]

    recipe_url = "http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s" % (app_id, app_key)


    for term in terms:
        res = requests.get("%s&allowedCourse[]=&q=%s" % (recipe_url, term))
        print res.json()
        if res.json():
            for a in res.json()['matches']:

                print a
                recipe_id =  a["id"]
                recipe_name = a["recipeName"]
                recipe_image_url = a["imageUrlsBySize"]["90"]
                #print a["ingredients"]
                print "\n"

                recipe = Recipe(name=recipe_name, image_url=recipe_image_url)
                recipe.save()
    return HttpResponse(json.dumps(res.json()), content_type="application/json")