from django.urls import path, re_path
from .views import VideoList, VideoDetail, CategoryDetail, SearchResult

app_name = 'videos'

urlpatterns = [
    path('', VideoList.as_view(), name='all videos'),
    re_path(r'video_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', VideoDetail.as_view(), name='video detail'),
    re_path(r'category_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', CategoryDetail.as_view(), name='category detail'),
    path("search_result/", SearchResult.as_view(), name='search result'),
]
