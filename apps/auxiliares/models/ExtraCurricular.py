from django.db import models
from apps.cuenta.models import User

class ActividadExtraCurricular(models.Model):
    descripcion = models.CharField(max_length=255)
    estatus = models.BooleanField()

    class Meta:
        managed             = True
        db_table            = 'auxiliares\".\"actividad_extra_curricular'
        verbose_name        = 'Actividad extra curricular'
        verbose_name_plural = 'Actividades extra curriculares'

    def __str__(self):
        return self.descripcion
