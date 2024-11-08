from django.db import models
from apps.cuenta.models import User

class Voceria(models.Model):
    descripcion = models.CharField(max_length=255)
    estatus = models.BooleanField()

    class Meta:
        managed             = True
        db_table            = 'auxiliares\".\"voceria'
        verbose_name        = 'Voceria'
        verbose_name_plural = 'Vocerias'

    def __str__(self):
        return self.descripcion
