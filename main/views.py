import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
from models import Recipe, Ingredient, User
import util, forms

def home(request):
    page_info = {"page_title": "Home"}
    if all(info in request.session for info in ['age', 'gender', 'style']):
        return redirect('/dashboard')
    else:
        return render(request, 'home.html', {"page_info": page_info,
                                             "hide_links": True})

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
                print res.json()
                if res.json() and res.json()['matches']:
                    a = res.json()['matches'][0]
                    print a
                    servings = specific_res['numberOfServings']

                    recipe_id =  a["id"]
                    recipe_name = a["recipeName"]
                    recipe_image_url = a["smallImageUrls"][0] + "0"
                    ingredients = a["ingredients"]
                    ingredients = json.dumps(ingredients)
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
                        if not Recipe.objects.filter(name=recipe_name):
                            recipe = Recipe(name=recipe_name,
                                            image_url=recipe_image_url,
                                            ingredients_json=ingredients,
                                            recipe_json=json.dumps(a),
                                            prep_time_seconds=prep_time_seconds,
                                            steps_json=instructions,
                                            is_vegetarian=is_vegetarian,
                                            servings=servings)
                            recipe.save()
                        else:
                            print "ignoring duplicate\n"
                else:
                    print "err\n"
        else:
            print "err\n"

    ingredients = Ingredient.objects.all()[:200];
    page_info = {"page_title": "Improve",
                 "ingredients": ingredients}
    return render(request, 'improve.html', {"page_info": page_info})


def dashboard(request):
    make_user = True
    user = None
    if request.session.get('unique_id'):
        # get their stuff from db
        user = User.objects.filter(id=request.session['unique_id']).first()

    if not user:
        user = User()
        user.save()
        request.session['unique_id'] = user.id

    # save preferences sent via POST
    # TODO: check if all values are set
    if request.method == 'POST':
        request.session['age'] = request.POST['age']
        request.session['gender'] = request.POST['gender']
        request.session['style'] = request.POST['style']
        # save user in db
        user.is_vegetarian = (request.POST['style'] == "vegetarian");
        user.age = int(request.POST['age']);
        user.gender = int(request.POST['gender'] == 'm');
        user.save()

    # redirect if preferences are not available via session
    # elif not all(info in request.session for info in ['age', 'gender', 'style']):
    #     return redirect('/')
    #
    # user_age = request.session['age']
    # user_gender = request.session['gender']
    # user_style = request.session['style']
    # print "User prefs: %s, %s, %s" % (user_age, user_gender, user_style)
    #TODO: do some math with the preferences


    day = datetime.datetime.now().weekday()

    num_to_show = 7

    # TODO orderby ? is slow
    if user.is_vegetarian:
        recipes = Recipe.objects.order_by('?')[:num_to_show]
    else:
        recipes = Recipe.objects.filter(is_vegetarian=True).order_by('?')[:num_to_show]
    for recipe in recipes:
        recipe.day = util.day_string(day)
        recipe.day_no = day
        day = (day + 1) % 7
    page_info = {"page_title": "Dashboard"}
    return render(request, 'dashboard.html', {"page_info": page_info,
                                              "recipes": recipes})
