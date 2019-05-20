from django import forms

class LoginForm(forms.Form):
    usr = forms.CharField(label="username")
    pwd = forms.CharField(label='password', widget=forms.PasswordInput())


class SignupForm(forms.Form):
    usr = forms.CharField(label="username")
    pwd = forms.CharField(label='password', widget=forms.PasswordInput())
    pwd_cnf = forms.CharField(label='confirm_password', widget=forms.PasswordInput())
    name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="e-mail")