from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    usr = forms.CharField(label="username")
    pwd = forms.CharField(label='password', widget=forms.PasswordInput())


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="e-mail")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user