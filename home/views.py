from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView


class HomePage(TemplateView):
    template_name = 'home/index.html'
