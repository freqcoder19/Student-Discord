from django.forms import ModelForm
from django import forms
from .models import User, Room  # Adjust the import according to your User model's location

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # Adjust according to your Room model fields

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

