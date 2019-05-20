from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm

class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()

        context = {'form': form}
        return render(request, 'users/login.html', context)

