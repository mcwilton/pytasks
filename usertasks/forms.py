from django import forms
from .models import Current


class CurrentForm(forms.ModelForm):
    class Meta:
        model = Current
        fields = '__all__'
