from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from base.models import Character


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.Form):
    avatar = forms.ModelChoiceField(
        queryset=Character.objects.all(), required=False)
    username = forms.CharField()
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea, required=False)
