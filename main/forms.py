from django import forms

class YummlyForm(forms.Form):
    yummly_id = forms.TextInput()