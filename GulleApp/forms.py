from django import forms
from django.contrib.auth.models import User
from .models import Message, Profile

class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'date', 'time' ,]

        widgets={
        'date': forms.DateInput(attrs={'type':'date'}),
        'time': forms.TimeInput(attrs={'type':'time'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date',]

        widgets={
        'birth_date': forms.DateInput(attrs={'type':'date'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


