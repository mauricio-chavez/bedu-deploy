"""Utilitary models for the songs app"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class SongsAppModel(models.Model):
    """This model will serve as base model for every model in this project

    It includes a name, timestamps, a __str__ method and orders by name
    """
    name = models.CharField(_('nombre'), max_length=100)
    created_at = models.DateTimeField(
        verbose_name=_('fecha de creación'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(_('última actualización'), auto_now=True)

    def __str__(self):
        """Returns model string representation"""
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']
