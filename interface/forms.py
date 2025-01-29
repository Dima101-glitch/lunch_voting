from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django import forms

from api.models import Employee


class ProfileForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'username', 'restaurant']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-select'}),
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = Employee
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'restaurant']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-select'}),
        }
