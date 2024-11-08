from django.db import models
from apps.cuenta.models import User
from apps.auxiliares.models.Voceria import Voceria
from apps.auxiliares.models.ExtraCurricular import ActividadExtraCurricular

class Asistente(models.Model):
    V    =   'V'
    E    =   'E'

    ORIGEN  =   (
                    (V,  'V'),
                    (E,  'E'),
                )
    
    primer_nombre = models.CharField(max_length=100, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    origen = models.CharField(max_length=1)
    cedula = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=10)
    cod_plantel = models.CharField(max_length=50)
    institucion_educativa = models.CharField(max_length=255)
    anio_curso = models.CharField(max_length=10)
    voceria = models.ForeignKey(Voceria, on_delete=models.PROTECT)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    numero_telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    usuario_instagram = models.CharField(max_length=100, blank=True, null=True)
    usuario_tiktok = models.CharField(max_length=100, blank=True, null=True)
    extra_curricular = models.ForeignKey(ActividadExtraCurricular, on_delete=models.PROTECT)
    identificador = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs): 
        self.identificador = self.origen + str(self.cedula)
        super(Asistente, self).save(*args, **kwargs)

    class Meta:
        managed             = True
        db_table            = 'feveem\".\"asistente'
        verbose_name        = 'Asistente'
        verbose_name_plural = 'Asistentes'
        unique_together     = ('cedula', 'origen',)
        
    def __str__(self):
        return f'{self.primer_nombre} {self.primer_apellido}'
