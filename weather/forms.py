# In weather/forms.py

from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='Enter Location')
