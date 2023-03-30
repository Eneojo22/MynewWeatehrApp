from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('photos', views.photos, name='photos'),
    path('single', views.single, name='single'),
    path('live-cameras', views.live_cameras, name='live_cameras'),
    ]
