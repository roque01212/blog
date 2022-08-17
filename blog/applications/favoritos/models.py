from django.db import models
from django.conf import settings
# apps de terceros
from model_utils.models import TimeStampedModel
#
from applications.entrada.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """Modelo para favoritos"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_favorites'
    )
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        related_name='entry_favorites',
    )
    objects=FavoritesManager()

    class Meta:
        unique_together=('user', 'entry')
        verbose_name='Entrada Favorita'
        verbose_name_plural='Entradas favoritas'

    def __str__(self):
        return f"{ self.entry.title} {self.id}"