from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'cols': 30})
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_admin = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_admin = forms.BooleanField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_admin')


