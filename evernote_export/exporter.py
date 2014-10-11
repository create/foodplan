import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import time

from evernote.api.client import EvernoteClient

from main.models import Recipe


class EvernoteExporter():
    def __init__(self, sandbox=True):
        self.sandbox = sandbox
        self.notebook_name = "Groceries"

        self.auth_token_real = "S=s344:U=371ef6d:E=150580d1802:C=149005be9c0:P=1cd:A=en-devtoken:V=2:H=5f5cb18a5e1755a7facdff9e44b7b411"
        self.auth_token_sandbox = "S=s1:U=8fa5d:E=150581d5082:C=149006c2218:P=1cd:A=en-devtoken:V=2:H=e59f1fe3b6442900f944689ea7ecff55"

        if self.sandbox:
            auth_token = self.auth_token_sandbox
        else:
            auth_token = self.auth_token_real

        self.client = EvernoteClient(token=auth_token, sandbox=self.sandbox)
        self._check_api_version()
        self.note_store = self.client.get_note_store()

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

    def _get_notebook_guid(self):
        notebooks = self.note_store.listNotebooks()

        target_notebook = ''
        for notebook in notebooks:
            if notebook.name == self.notebook_name:
                target_notebook = notebook
                break

        if target_notebook == '':
            print 'Notebook Groceries does not exist'
            exit(1)

        return target_notebook.guid

    def _create_note(self, title, content):
        note = Types.Note()
        note.title = title
        note.notebookGuid = self._get_notebook_guid()

        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM ' \
            '"http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>'
        note.content += content
        note.content += '</en-note>'

        created_note = self.note_store.createNote(note)
        return created_note.guid

    def export_recipe(self, item):
        title = "Groceries List " + item.name

        content = ''
        content += '<div>' + item.instructions +'</div>'
        content += '<div><br></div>'
        content += '<div>' + item.ingredients +'</div>'

        return self._create_note(title, content)

    def export_grocery_list(self, items):
        title = "Groceries List " + time.strftime("%H:%M %d/%m/%Y").__str__()

        content = ''
        for item in items:
            print item
            content += '<div><en-todo/>' + item['name'] + '</div>'

        return self._create_note(title, content)


# USAGE EXAMPLE
first = False
second = True

if first:
    items = [{'name': 'TEST1'}, {"name": "TEST2"}]
    exporter = EvernoteExporter(sandbox=True)
    # save guid for editing the note
    guid = exporter.export_grocery_list(items)

if second:
    pass