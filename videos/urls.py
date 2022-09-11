from django.urls import path
from .views import VideoList

app_name = 'videos'

urlpatterns = [
    path('', VideoList.as_view(), name='all videos')
]