import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from models import Recipe, Ingredient
import util, forms

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
    if request.method == 'POST':
        print request.POST
        app_id = "e91111f8"
        app_key = "f9d16213fe4a2371bb8c919c89dc409a"
        recipe_id = request.POST['yummly-id']
        instructions = []
        for i in range(1,5):
            if request.POST['step-%d' % i]:
                instructions.append(request.POST['step-%d' % i])
        recipe_id_url = "http://api.yummly.com/v1/api/recipe/%s?_app_id=%s&_app_key=%s" % (recipe_id, app_id, app_key)
        specific_res = requests.get(recipe_id_url).json()

        print specific_res

        terms = [specific_res['name']]

        recipe_url = "http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s" % (app_id, app_key)

        for term in terms:
            res = requests.get("%s&allowedCourse[]=&q=%s" % (recipe_url, term))
            print res.json()
            if res.json() and res.json()['matches']:
                a = res.json()['matches'][0]
                print a
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
                instructions = ["If you're cooking chicken for this, trim visible fat from 4 chicken breasts, then cut the chicken lengthwise into thirds.  Put the can of chicken stock, 2 cans of water, and the Italian Herb Blend into a small sauce pan and bring to a boil.  When it boils add chicken breasts, turn heat to medium low, and  let simmer 15-20 minutes, or until the chicken is cooked through.  Drain the chicken into a colander placed in the sink and let it cool.  (I saved the liquid in the freezer to add when I'm making chicken stock.)'In a large skillet, melt butter over medium; reserve 1 tablespoon in a small bowl. To skillet, add apples, 1/2 cup sugar, and cinnamon. Increase heat to medium-high; cook, tossing occasionally, until apples are tender and liquid has evaporated, about 15 minutes. Spread filling on a second rimmed baking sheet; let cool completely.",
                                "While the chicken cools, slice the basil leaves (and wash if needed), chop green onions, and measure the freshly-grated Parmesan. When it's cool, dice chicken into pieces about 3/4 inch square and place into medium-sized bowl.",
                                "Combine mayo and buttermilk, whisking until it's smooth.  Then stir in green onion, Parmesan, and basil. Add dressing to the chicken in the bowl and gently mix until chicken is well coated with dressing. Season with salt and fresh ground black pepper. This can be served immediately or chilled slightly before serving.  This will keep in the fridge for about a day, but it's best freshly made."]
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
