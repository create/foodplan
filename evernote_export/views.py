from django.shortcuts import render
from main.models import Recipe
from exporter import EvernoteExporter
from django import http
import json


def export_recipe(request, id):
    return http.HttpResponse(id)

def test(request):
    exporter = EvernoteExporter(sandbox=True)
    rs = Recipe.objects.all()[:2]
    exporter.import_meals(rs)

    return http.HttpResponse("OK")

    for r in rs:
        print r.name
        print '===='

        ds = json.loads(r.ingredients_json)
        for d in ds:
            print d

        ss = json.loads(r.steps_json)
        for s in ss:
            print s

        print '+++'


