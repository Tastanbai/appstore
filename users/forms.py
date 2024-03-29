
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField()
    class Meta:
        model = User
    fields=['username','password']

class UserRegistrationForm(UserCreationForm):
    class Meta: 
        model=User
        fields=(
            "last_name",
            "first_name",
            "username",
            "email",
            "password1",
            "password2"
        )    

        last_name=forms.CharField()
        first_name=forms.CharField()
        username=forms.CharField()
        email=forms.CharField()
        password1=forms.CharField()
        password2=forms.CharField()