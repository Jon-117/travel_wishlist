from django import forms
from .models import Place


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'visited']
        # fields = ['name', 'visited', 'user', 'notes', 'date_visited', 'photo']
