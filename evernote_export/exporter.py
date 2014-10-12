import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import time
import json

from evernote.api.client import EvernoteClient

from main.models import Recipe


class EvernoteExporter():
    def __init__(self, sandbox=True):
        self.sandbox = sandbox

        self.ingredients = {}
        self.recipes = []

        self.auth_token_real = "S=s344:U=371ef6d:E=150580d1802:C=149005be9c0:P=1cd:A=en-devtoken:V=2:H=5f5cb18a5e1755a7facdff9e44b7b411"
        self.auth_token_sandbox = "S=s1:U=8fa5d:E=150581d5082:C=149006c2218:P=1cd:A=en-devtoken:V=2:H=e59f1fe3b6442900f944689ea7ecff55"

        if self.sandbox:
            auth_token = self.auth_token_sandbox
        else:
            auth_token = self.auth_token_real

        self.client = EvernoteClient(token=auth_token, sandbox=self.sandbox)
        self._check_api_version()
        self.note_store = self.client.get_note_store()

        self.notebook_name_for_groceries = "Pantry Groceries"
        self.notebook_name_for_recipes = "Pantry Recipes"

    def _check_api_version(self):
        user_store = self.client.get_user_store()
        version_ok = user_store.checkVersion(
            "Evernote EDAMTest (Python)",
            UserStoreConstants.EDAM_VERSION_MAJOR,
            UserStoreConstants.EDAM_VERSION_MINOR
        )
        print "Is my Evernote API version up to date? ", str(version_ok)
        print ""
        if not version_ok:
            exit(1)

    def _get_notebook_guid(self, name):
        notebooks = self.note_store.listNotebooks()

        target_notebook = ''
        for notebook in notebooks:
            if notebook.name == name:
                target_notebook = notebook
                break

        if target_notebook == '':
            print 'Notebook does not exist'
            exit(1)

        return target_notebook.guid

    def _create_note(self, title, content, guid):
        note = Types.Note()
        note.title = title
        note.notebookGuid = guid

        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM ' \
            '"http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>'
        note.content += content
        note.content += '</en-note>'

        created_note = self.note_store.createNote(note)
        return created_note.guid

    def export_recipe(self, item):
        if item.id in self.recipes:
            return None
        else:
            self.recipes.append(item.id)

        title = "Recipe: " + item.name

        content = ''
        content += '<div><b>Name:</b>' + item.name + '</div>'
        content += '<div><br/></div>'
        content += self._create_steps_list(item.steps_json)
        content += '<div><br/></div>'
        content += self._create_ingredients_list(item.ingredients_json)

        guid = self._get_notebook_guid(self.notebook_name_for_recipes)

        return self._create_note(title, content, guid)

    def export_grocery_list(self):
        items = self.ingredients
        print items
        title = "Groceries List " + time.strftime("%H:%M %d/%m/%Y").__str__()

        content = ''
        for name in items:
            content += '<div><en-todo/>' + name + '</div>'

        guid = self._get_notebook_guid(self.notebook_name_for_groceries)

        return self._create_note(title, content, guid)

    def _create_steps_list(self, steps_json):
        sl = json.loads(steps_json)
        content = ''
        content += '<div><b>Steps:</b></div>'
        for s in sl:
            content += '<div>' + s + '</div>'

        return content

    def _create_ingredients_list(self, ingredients_json):
        il = json.loads(ingredients_json)
        content = ''
        content += '<div><b>Ingredients:</b></div>'
        for i in il:
            content += '<div>' + i + '</div>'

        return content

    def _add_to_ingredient_list(self, item):
        if item in self.ingredients:
            self.ingredients[item] += 1
        else:
            self.ingredients[item] = 1

    def import_meals(self, meals_list):
        for meal in meals_list:
            recipe = Recipe.objects.get(pk=meal.recipe_id)
            # TODO uncomment this section
            self.export_recipe(recipe)
            il = json.loads(recipe.ingredients_json)
            for i in il:
                self._add_to_ingredient_list(i)
            print recipe.name + " | " + str(meal.date)


        self.export_grocery_list()


# USAGE EXAMPLE
first = False

if first:
    items = [{'name': 'TEST1'}, {"name": "TEST2"}]
    exporter = EvernoteExporter(sandbox=True)
    # save guid for editing the note
    guid = exporter.export_grocery_list(items)
