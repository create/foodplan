import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from models import Recipe, Ingredient, User, ScheduledMeal
import util, forms
import re, posixpath, urlparse
from evernote_export.exporter import EvernoteExporter

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
    ingredients = Ingredient.objects.all()[:20]
    print len(ingredients)
    return render(request, 'pantry.html', {"page_info": page_info,
                                           "ingredients": ingredients})


def about(request):
    page_info = {"page_title": "About"}
    return render(request, 'about.html', {"page_info": page_info})


def improve(request):
    show_success = False
    show_error = False
    show_already = False
    try:
        if request.method == 'POST':
            print request.POST
            app_id = "e91111f8"
            app_key = "f9d16213fe4a2371bb8c919c89dc409a"
            recipe_id = request.POST['yummly-id']

            # extract actual recipe id if recipe_id is a url
            if not re.match('^[\w-]+$', recipe_id):
                print "rematch"
                recipe_id = posixpath.basename(urlparse.urlsplit(recipe_id).path)
                print recipe_id

            instructions = []
            for i in range(1,5):
                if request.POST['step-%d' % i]:
                    instructions.append(request.POST['step-%d' % i])

            instructions = json.dumps(instructions)
            recipe_id_url = "http://api.yummly.com/v1/api/recipe/%s?_app_id=%s&_app_key=%s" % (recipe_id, app_id, app_key)
            specific_res = requests.get(recipe_id_url)
            if specific_res:
                specific_res = specific_res.json()
                print specific_res

                terms = [specific_res['name']]

                recipe_url = "http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s" % (app_id, app_key)

                for term in terms:
                    res = requests.get("%s&allowedCourse[]=&q=%s" % (recipe_url, term))
                    # print res.json()
                    if res.json() and res.json()['matches']:
                        a = res.json()['matches'][0]

                        servings = specific_res['numberOfServings']

                        recipe_id =  a["id"]
                        recipe_name = a["recipeName"]
                        recipe_image_url = a["smallImageUrls"][0] + "0"
                        ingredients = a["ingredients"]
                        ingredients = json.dumps(ingredients)
                        is_vegetarian = (request.POST.get('meal_is_vegetarian', False) == 'on')
                        print is_vegetarian
                        price = int(request.POST.get('price', 8) or 8)
                        # for meat in ['turkey', 'beef', 'meat', 'steak', 'chicken', 'pork', 'bacon', 'ham', 'duck', 'goose']:
                        #     if any(meat in s for s in ingredients):
                        #         is_vegetarian = False

                        prep_time_seconds = a["totalTimeInSeconds"]
                        instructions = ["If you're cooking chicken for this, trim visible fat from 4 chicken breasts, then cut the chicken lengthwise into thirds.  Put the can of chicken stock, 2 cans of water, and the Italian Herb Blend into a small sauce pan and bring to a boil.  When it boils add chicken breasts, turn heat to medium low, and  let simmer 15-20 minutes, or until the chicken is cooked through.  Drain the chicken into a colander placed in the sink and let it cool.  (I saved the liquid in the freezer to add when I'm making chicken stock.)'In a large skillet, melt butter over medium; reserve 1 tablespoon in a small bowl. To skillet, add apples, 1/2 cup sugar, and cinnamon. Increase heat to medium-high; cook, tossing occasionally, until apples are tender and liquid has evaporated, about 15 minutes. Spread filling on a second rimmed baking sheet; let cool completely.",
                                        "While the chicken cools, slice the basil leaves (and wash if needed), chop green onions, and measure the freshly-grated Parmesan. When it's cool, dice chicken into pieces about 3/4 inch square and place into medium-sized bowl.",
                                        "Combine mayo and buttermilk, whisking until it's smooth.  Then stir in green onion, Parmesan, and basil. Add dressing to the chicken in the bowl and gently mix until chicken is well coated with dressing. Season with salt and fresh ground black pepper. This can be served immediately or chilled slightly before serving.  This will keep in the fridge for about a day, but it's best freshly made."]
                        if not (prep_time_seconds and ingredients and recipe_id and recipe_name and recipe_image_url and prep_time_seconds):
                            print "Not enough information, try a different recipe\n"
                        else:
                            if not Recipe.objects.filter(name=recipe_name):
                                recipe = Recipe(name=recipe_name,
                                                image_url=recipe_image_url,
                                                ingredients_json=ingredients,
                                                recipe_json=json.dumps(a),
                                                detailed_json=json.dumps(specific_res),
                                                prep_time_seconds=prep_time_seconds,
                                                steps_json=instructions,
                                                is_vegetarian=is_vegetarian,
                                                price=price,
                                                servings=servings)
                                recipe.save()
                                show_success=True
                            else:
                                print "ignoring duplicate\n"
                                show_already = True
                    else:
                        print "err\n"
                        show_error = True
            else:
                print "err\n"
                show_error = True
    except:
        show_error = True
    page_info = {"page_title": "Improve"}
    return render(request, 'improve.html', {"page_info": page_info,
                                            "show_success": show_success,
                                            "show_error": show_error,
                                            "show_already": show_already})


def dashboard(request):
    make_user = True
    user = None

    # save preferences sent via POST
    # TODO: check if all values are set
    if request.method == 'POST':
        user = User()
        user.save()
        request.session['unique_id'] = user.id

        try:
            request.session['age'] = int(request.POST.get('age', 20) or 20)
        except:
            request.session['age'] = 20

        request.session['name'] = request.POST.get('name', 'Hi') or 'Hi'

        request.session['gender'] = request.POST.get('gender', 'm')

        request.session['style'] = request.POST.get('style', 'classic')

        # save user in db
        user.is_vegetarian = (request.POST.get('style', 'classic') == "vegetarian")
        user.age = int(request.session.get('age', 20) or 20)
        user.gender = int(request.POST.get('gender', 'm') == 'm')
        user.save()
    elif request.session.get('unique_id'):
        # get their stuff from db
        user = User.objects.filter(id=request.session['unique_id']).first()
    else:
        user = User()
        user.save()

    now = datetime.datetime.now()
    day = now.weekday()

    num_to_show = 7

    # TODO orderby('?') is slow
    today = now.date()
    recipes = []
    for i in range(0, num_to_show):
        meal = ScheduledMeal.objects.filter(date=today).filter(user_id=user.id).first()
        ids_to_exclude = (recipe.id for recipe in recipes)
        if not meal:
            if not user.is_vegetarian:
                recipe_id = _get_random_recipe(False, ids_to_exclude)
            else:
                recipe_id = _get_random_recipe(True, ids_to_exclude)

            if recipe_id:
                recipe_id = recipe_id.id
                meal = ScheduledMeal(date=today, user_id=user.id, recipe_id=recipe_id)
                meal.save()
        if meal:
            recipe = Recipe.objects.filter(id=meal.recipe_id).first()
            if recipe:
                recipes.append(recipe)
        today = today + datetime.timedelta(days=1)

    total_price = 0.
    for recipe in recipes:
        total_price += float(recipe.price)
        recipe.day = util.day_string(day)
        recipe.day_no = day
        day = (day + 1) % 7

        try:
            detailed_json = json.loads(recipe.detailed_json)
            recipe.ingredient_lines = detailed_json["ingredientLines"]
        except ValueError:
            recipe.ingredient_lines = []

        recipe.prep_time = recipe.prep_time_seconds / 60


    total_price = "%.2f" % total_price
    page_info = {"page_title": "Dashboard"}
    return render(request, 'dashboard.html', {"page_info": page_info,
                                              "recipes": recipes, "total_price": total_price, "username": request.session.get("name", "Hi")})

def _get_random_recipe(is_vegetarian=False, ids_to_exclude=None):
    if not ids_to_exclude:
        ids_to_exclude = []
    if is_vegetarian:
        return Recipe.objects.filter(is_vegetarian=True).exclude(id__in=ids_to_exclude).order_by('?').first()
    else:
        return Recipe.objects.exclude(id__in=ids_to_exclude).order_by('?').first()

def reroll(request):
    response = {}
    response['result'] = 'error'
    if request.GET.get('day', False):
        user = User.objects.filter(id=request.session.get('unique_id')).first()
        day = int(request.GET.get('day'))
        today = datetime.datetime.now().date()
        delta = (day - today.weekday()) % 7
        day_to_reroll = today + datetime.timedelta(days=delta)
        meal = ScheduledMeal.objects.filter(date=day_to_reroll).filter(user_id=user.id).first()
        recipe = _get_random_recipe(user.is_vegetarian)
        old_id = meal.recipe_id
        old_recipe = Recipe.objects.get(id=old_id)
        meal.recipe_id = recipe.id
        meal.save()
        response['result'] = {'image_url': recipe.image_url,
            'name': recipe.name,
            'price': str(recipe.price),
            'total_price_change': str(recipe.price - old_recipe.price)
        }

    return HttpResponse(json.dumps(response), content_type='application/json')

def export(request):
    user = None
    if request.session.get('unique_id'):
        # get their stuff from db
        user = User.objects.filter(id=request.session['unique_id']).first()

    meals = ScheduledMeal.objects.filter(user_id=user.id).filter(date__gte=datetime.datetime.now().date()).extra(order_by=['date']).all()[:4]
    print len(meals)

    exporter = EvernoteExporter(sandbox=False)
    exporter.import_meals(meals)
    response = {}
    response['result'] = 'Done'
    return HttpResponse(json.dumps(response), content_type='application/json')
