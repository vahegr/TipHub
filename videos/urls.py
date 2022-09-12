from django.urls import path
from .views import VideoList, VideoDetail

app_name = 'videos'

urlpatterns = [
    path('', VideoList.as_view(), name='all videos'),
    path('video_detail/<int:id>/<slug:slug>', VideoDetail.as_view(), name='video detail')
]