from django.db import models


class Recipe(models.Model):
    #id = models.CharField()
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    #description = models.CharField()

    class Meta:
        app_label = 'main'

#class Ingredient(models.Model):
    #name = models.CharField(max_length=255)
