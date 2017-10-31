"""tunr_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.artist_list, name='artist_list'),
    url(r'^songs$', views.song_list, name='song_list'),
    url(r'^artists/(?P<pk>\d+)$', views.artist_detail, name='artist_detail'),
    url(r'^songs/(?P<pk>\d+)$', views.song_detail, name='song_detail'),
    url(r'^artists/new$', views.artist_create, name='artist_create'),
    url(r'^songs/new$', views.song_create, name='song_create'),
    url(r'^artists/(?P<pk>\d+)/edit$', views.artist_edit, name='artist_edit')
]
