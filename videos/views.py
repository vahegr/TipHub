from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, RedirectView
from .models import Video, Category, Like, Comment


class VideoList(ListView):
    paginate_by = 9
    model = Video
    template_name = 'videos/all-videos.html'
    queryset = Video.objects.filter(allowing=True)


def video_detail(request, id, slug):
    video = get_object_or_404(Video, id=id, slug=slug)
    ip_address = request.user.ip_address
    if ip_address not in video.hits.all():
        video.hits.add(ip_address)
    is_liked = None
    if request.user.is_authenticated:
        if request.user.likes.filter(video_id=id, video__slug=slug, user_id=request.user.id).exists():
            is_liked = True
        else:
            is_liked = False

    # comments pagination
    comments = video.comments.all()
    pagination = Paginator(comments, 5)
    page = request.GET.get('page')
    obj_pagination = pagination.get_page(page)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        parent = request.POST.get('parent_id')
        Comment.objects.create(comment=comment, video=video, user=request.user, parent_id=parent)

    return render(request, "videos/video-detail.html", context={'object': video, 'is_liked': is_liked, 'comments': obj_pagination})


def comment_delete(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=pk)
        video_id = comment.video.id
        video_slug = comment.video.slug
        comment.delete()
        return redirect(reverse('videos:video detail', kwargs={'id': video_id, 'slug': video_slug}))
    else:
        return redirect('home:home')


def video_like(request, id, slug):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(video_id=id, video__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({'response': 'unliked'})
        except:
            Like.objects.create(video_id=id, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})


class CategoryDetail(ListView):
    paginate_by = 9
    template_name = 'videos/all-videos.html'

    def get_queryset(self):
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, id=id, slug=slug)
        return category.video_set.all()


class SearchResult(ListView):
    paginate_by = 9
    template_name = 'videos/all-videos.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        videos = Video.objects.filter(allowing=True, title__icontains=q)
        return videos
