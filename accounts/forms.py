from django import forms
from .models import Preferences

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )

class Signup_Form(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = [
            'display_mode'
        ]
