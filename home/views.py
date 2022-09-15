from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from videos.models import Video


class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_list'] = Video.objects.filter(allowing=True)[:6]
        return context
