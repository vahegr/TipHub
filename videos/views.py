from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Video, Category


class VideoList(ListView):
    model = Video
    template_name = 'videos/all-videos.html'
    queryset = Video.objects.filter(allowing=True)


class VideoDetail(DetailView):
    template_name = 'videos/video-detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        id = self.kwargs.get('id')
        video = Video.objects.get(id=id, slug=slug)
        ip_address = self.request.user.ip_address
        if ip_address not in video.hits.all():
            video.hits.add(ip_address)
        return video


class CategoryDetail(ListView):
    template_name = 'videos/all-videos.html'

    def get_queryset(self):
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, id=id, slug=slug)
        return category.video_set.all()
