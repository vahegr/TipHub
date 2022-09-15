from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import LogInForm


class UserLogIn(View):
    def get(self, request):
        if request.user.is_authenticated is True:
            return redirect('home:home')
        form = LogInForm()
        return render(request, 'account/login.html', context={'form': form})

    def post(self, request):
        if request.user.is_authenticated is True:
            return redirect('home:home')
        form = LogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                form.add_error('email', 'اطلاعات وارد شده اشتباه است')
        else:
            form.add_error('email', 'اطلاعات وارد شده اشتباه است')

        return render(request, 'account/login.html', context={'form': form})


class UserLogOut(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')
