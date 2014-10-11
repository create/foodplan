from django.shortcuts import render
from main.models import Recipe
from exporter import EvernoteExporter

def test(request):
    #exporter = EvernoteExporter(sandbox=True)
    rs = Recipe.objects.all()
    for r in rs:
        print r