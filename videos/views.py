from django.shortcuts import render
from django.views.generic import ListView, DetailView


class VideoList(ListView):
    template_name = 'videos/all-videos.html'
