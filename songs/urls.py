"""Songs app URL config"""

from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    path('', views.AlbumListView.as_view(), name='list'),
    path('create-album', views.AlbumCreateView.as_view(), name='create_album'),
]
