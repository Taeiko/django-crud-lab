from django import forms
from .models import Console

class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Console
        fields = ['name', 'release_year', 'is_worth_playing']