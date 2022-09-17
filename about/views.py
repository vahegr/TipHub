from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import About


class AboutUs(TemplateView):
    template_name = 'about/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.filter(allowing=True)
        return context
