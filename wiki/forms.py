from django import forms

class WikiLinkForm(forms.Form):
  title = forms.CharField(max_length=100)