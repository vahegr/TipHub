from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.UserLogIn.as_view(), name='log in'),
    path('logout', views.UserLogOut.as_view(), name='log out'),
]
