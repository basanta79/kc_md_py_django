from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from users.forms import LoginForm, SignupForm
from blogs.models import Blog


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()

        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'usuario o contraseña incorrectos')
            else:
                django_login(request, user)
                return redirect('home')
        context = { 'form': form }
        return render(request, 'users/login.html', context)


class Logout(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')


class Signup(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            first_blog = Blog(owner=user, title=user.first_name + ' first Blog')
            first_blog.save()
            return redirect('home')
        context = {'form': form}
        return render(request, 'users/login.html', context)