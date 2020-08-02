from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class KitchnForm(forms.Form):
    KitchenName= forms.CharField( max_length=100, required=True)
    ingredients = forms.CharField(max_length=100, required=True)
    