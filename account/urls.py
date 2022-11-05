from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.UserLogIn.as_view(), name='log in'),
    path('logout', views.UserLogOut.as_view(), name='log out'),
    re_path(r'profile/(?P<id>[0-9]+)/(?P<username>[-\w]+)/', views.UserProfile.as_view(), name='profile'),
    path('edit_profile', views.edit_profile, name='edit profile'),
]
