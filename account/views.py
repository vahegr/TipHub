from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.views.generic import DetailView
from .forms import LogInForm, EditProfileForm
from .models import User


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


class UserProfile(DetailView):
    template_name = 'account/user-panel.html'

    def get_object(self):
        id = self.kwargs.get('id')
        username = self.kwargs.get('username')
        return get_object_or_404(User, id=id, username=username)


def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = EditProfileForm(instance=user)
        if request.method == 'POST':
            form = EditProfileForm(instance=user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('account:profile', kwargs={'id': request.user.id, 'username': request.user.username}))
        return render(request, "account/edit-user-panel.html", context={'form': form})
