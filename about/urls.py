from django.urls import path
from .views import AboutUs

app_name = 'about'

urlpatterns = [
    path('', AboutUs.as_view(), name='about_us'),
]