"""Songs app views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Album


class AlbumListView(LoginRequiredMixin, ListView):
    """Track list view"""
    model = Album
    template_name = "songs/list.html"


class AlbumCreateView(LoginRequiredMixin, CreateView):
    """Creates a new album"""
    model = Album
    success_url = reverse_lazy('songs:list')
    template_name = "songs/create-album.html"
    fields = ['name', 'cover']
