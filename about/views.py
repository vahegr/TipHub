from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class AboutUs(TemplateView):
    template_name = 'about/about-us.html'
