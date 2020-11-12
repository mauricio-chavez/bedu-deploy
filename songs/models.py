"""Songs app models"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils.models import SongsAppModel


class Track(SongsAppModel):
    """Track model"""
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta(SongsAppModel.Meta):
        verbose_name = _('pista')


class Artist(SongsAppModel):
    """Artist model"""
    birthday = models.DateField()

    class Meta(SongsAppModel.Meta):
        verbose_name = _('artista')


class Album(SongsAppModel):
    """Album model"""
    cover = models.ImageField(_('portada'), upload_to='covers')

    class Meta(SongsAppModel.Meta):
        verbose_name = _('álbum')
        verbose_name_plural = _('álbumes')
