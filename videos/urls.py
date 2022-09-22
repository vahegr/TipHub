from django.urls import path, re_path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='all videos'),
    re_path(r'video_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.video_detail, name='video detail'),
    re_path(r'category_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.CategoryDetail.as_view(), name='category detail'),
    re_path(r'video_like/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.video_like, name='video like'),
    path("search_result/", views.SearchResult.as_view(), name='search result'),
]
