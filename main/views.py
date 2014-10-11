import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from models import Recipe, Ingredient
import util

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
    ingredients = Ingredient.objects.all()
    page_info = {"page_title": "Improve",
                 "ingredients": ingredients}
    return render(request, 'improve.html', {"page_info": page_info})


def dashboard(request):
    day = datetime.datetime.now().weekday()
    # orderby ? is slow
    recipes = Recipe.objects.order_by('?')[:5]
    for recipe in recipes:
        recipe.day = util.day_string(day)
        day = (day + 1) % 7
    page_info = {"page_title": "Dashboard"}
    return render(request, 'dashboard.html', {"page_info": page_info,
                                              "recipes": recipes})

def get_recipe(request):
    app_id = "e91111f8"
    app_key = "f9d16213fe4a2371bb8c919c89dc409a"

    # specify random healthy ingredients to get enough data out of the API
    #terms = ["carrot", "onion", "potato", "tomato", "cucumber"]
    terms = ["Apple-Cinnamon Strudel"]

    recipe_url = "http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s" % (app_id, app_key)



    for term in terms:
        res = requests.get("%s&allowedCourse[]=&q=%s" % (recipe_url, term))
        print res.json()
        if res.json() and res.json()['matches']:
            a = res.json()['matches'][0]
            print a
            recipe_id_url = "http://api.yummly.com/v1/api/recipe/%s?_app_id=%s&_app_key=%s" % (a["id"], app_id, app_key)
            specific_res = requests.get(recipe_id_url).json()
            servings = specific_res['numberOfServings']

            recipe_id =  a["id"]
            recipe_name = a["recipeName"]
            recipe_image_url = a["smallImageUrls"][0] + "0"
            ingredients = a["ingredients"]
            is_vegetarian = True
            for meat in ['turkey', 'beef', 'meat', 'steak', 'chicken', 'pork', 'bacon', 'ham', 'duck', 'goose']:
                if any(meat in s for s in ingredients):
                    is_vegetarian = False
            prep_time_seconds = a["totalTimeInSeconds"]
            instructions = ['Preheat oven to 400 degrees; line a baking sheet with parchment paper or foil. On a lightly floured work surface, unfold pastry; roll out to a 12-by-14-inch rectangle. Place on sheet; refrigerate.',
                            'In a large skillet, melt butter over medium; reserve 1 tablespoon in a small bowl. To skillet, add apples, 1/2 cup sugar, and cinnamon. Increase heat to medium-high; cook, tossing occasionally, until apples are tender and liquid has evaporated, about 15 minutes. Spread filling on a second rimmed baking sheet; let cool completely.',
                            'With one short side of dough facing you, mound filling horizontally in a strip across the center, leaving a 1-inch border on both long sides. Fold top part, then bottom part of dough over filling. Turn pastry over, seam side down.',
                            'Brush pastry with reserved melted butter; sprinkle with remaining 2 tablespoons sugar. Using a paring knife, cut steam vents in center of pastry. Bake until golden brown, 35 to 40 minutes. Let rest 10 minutes before serving.']
            if not (prep_time_seconds and ingredients and recipe_id and recipe_name and recipe_image_url and prep_time_seconds):
                print "Not enough information, try a different recipe\n"
            else:

                recipe = Recipe(name=recipe_name,
                                image_url=recipe_image_url,
                                ingredients=ingredients,
                                recipe_json=json.dumps(a),
                                prep_time_seconds=prep_time_seconds,
                                instructions=instructions,
                                is_vegetarian=is_vegetarian,
                                servings=servings)
                recipe.save()
        else:
            print "err\n"
    return HttpResponse(json.dumps(res.json()), content_type="application/json")
