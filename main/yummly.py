#!/usr/bin/env python2
# encoding: utf-8

import json
import requests

from django.conf import settings
settings.configure()

from django.db import models
from models import Recipe




app_id = "e91111f8"
app_key = "f9d16213fe4a2371bb8c919c89dc409a"

# specify random healthy ingredients to get enough data out of the API
#terms = ["carrot", "onion", "potato", "tomato", "cucumber"]
terms = ["carrot"]

recipe_url = "http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s" % (app_id, app_key)


for term in terms:
    res = requests.get("%s&allowedCourse[]=&q=%s" % (recipe_url, term))
    json_data = res.json()

    for a in json_data["matches"]:

        print a
        recipe_id =  a["id"]
        recipe_name = a["recipeName"]
        recipe_image_url = a["imageUrlsBySize"]["90"]
        #print a["ingredients"]
        print "\n"

        recipe = Recipe(name=recipe_name, image_url=recipe_image_url)
        recipe.save()


