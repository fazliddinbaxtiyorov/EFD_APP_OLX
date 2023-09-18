from django import forms
from .models import AddModels


class AddForm(forms.ModelForm):
    class Meta:
        model = AddModels
        fields = ['photo', 'title', 'description', 'categories', 'number', 'location', 'cost']

