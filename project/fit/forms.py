from django import forms 
from .models import fit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class fitForm(forms.ModelForm):
    class Meta:
        model=fit
        fields=['Firstname','Secondname','Email','Password']
