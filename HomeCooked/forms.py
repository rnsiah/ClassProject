from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Kitchn


class KitchnForm(forms.ModelForm):
    
    class Meta:
        model = Kitchn
        fields = ['legal name', 'address', 'phone number', ]

    