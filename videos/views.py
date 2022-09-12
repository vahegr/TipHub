from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video, Category


class VideoList(ListView):
    model = Video
    template_name = 'videos/all-videos.html'
    queryset = Video.objects.filter(allowing=True)
