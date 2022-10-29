from django.urls import path, re_path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='all videos'),
    re_path(r'video_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.video_detail, name='video detail'),
    re_path(r'category_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.CategoryDetail.as_view(), name='category detail'),
    re_path(r'video_like/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.video_like, name='video like'),
    path("search_result/", views.SearchResult.as_view(), name='search result'),
    re_path(r'delete_comment/(?P<pk>[0-9]+)/', views.comment_delete, name='delete comment'),
    re_path(r"read_notification/(?P<notif_id>[0-9]+)/", views.read_notification, name='read_notification'),
]
