import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import time

from evernote.api.client import EvernoteClient


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
            print "Groceries Notebook not found"
            return None

        return target_notebook.guid

    def export_grocery_list(self, items):
        note = Types.Note()
        note.title = "Groceries List " + time.strftime("%H:%M %d/%m/%Y").__str__()
        note.notebookGuid = self._get_notebook_guid()

        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM ' \
            '"http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note><br/>'
        for item in items:
            print item
            note.content += '<div><en-todo/>' + item['name'] + '</div>'
        note.content += '</en-note>'

        created_note = self.note_store.createNote(note)

        return created_note.guid


# USAGE EXAMPLE
# items = [{'name': 'item1'}, {"name": "item2"}]
# exporter = EvernoteExporter(sandbox=True)
# save guid for editing the note
# guid = exporter.export_grocery_list(items)