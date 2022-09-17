from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import About
from account.models import User


class AboutUs(TemplateView):
    template_name = 'about/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.filter(allowing=True)
        context['users'] = User.objects.filter(is_admin=True)
        return context
