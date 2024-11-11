from django.db import models

class Plantel(models.Model):

    estado = models.CharField(max_length=255, null=True, blank=True)
    periodo_escolar = models.CharField(max_length=255, null=True, blank=True)
    municipio = models.CharField(max_length=255, null=True, blank=True)
    parroquia = models.CharField(max_length=255, null=True, blank=True)
    cod_plantel = models.CharField(max_length=255, null=True, blank=True)
    nombre_plantel = models.CharField(max_length=255, null=True, blank=True)
    tipo_dependencia = models.CharField(max_length=255, null=True, blank=True)
    modalidad_principal = models.CharField(max_length=255, null=True, blank=True)
    estatus_plantel = models.CharField(max_length=255, null=True, blank=True)
    nivel_principal = models.CharField(max_length=255, null=True, blank=True)
    zona_ubicacion = models.CharField(max_length=255, null=True, blank=True)
    maternal_masculino = models.IntegerField(null=True, blank=True)
    maternal_femenino = models.IntegerField(null=True, blank=True)
    prescolar_masculino = models.IntegerField(null=True, blank=True)
    prescolar_femenino = models.IntegerField(null=True, blank=True)
    primaria_masculino = models.IntegerField(null=True, blank=True)
    primaria_femenino = models.IntegerField(null=True, blank=True)
    media_masculino = models.IntegerField(null=True, blank=True)
    media_femenino = models.IntegerField(null=True, blank=True)
    media_general_masculino = models.IntegerField(null=True, blank=True)
    media_general_femenino = models.IntegerField(null=True, blank=True)
    tecnica_masculino = models.IntegerField(null=True, blank=True)
    tecnica_femenino = models.IntegerField(null=True, blank=True)
    adulto_masculino = models.IntegerField(null=True, blank=True)
    adulto_femenino = models.IntegerField(null=True, blank=True)
    especial_masculino = models.IntegerField(null=True, blank=True)
    especial_femenino = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    director_nombre = models.CharField(max_length=255, null=True, blank=True)
    director_apellido = models.CharField(max_length=255, null=True, blank=True)
    tipo_documento = models.CharField(max_length=255, null=True, blank=True)
    documento_identidad = models.CharField(max_length=255, null=True, blank=True)
    telefono_director = models.CharField(max_length=255, null=True, blank=True)
    telefono_movil_director = models.CharField(max_length=255, null=True, blank=True)
    correo = models.EmailField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    
    peridoescolar = models.IntegerField(null=True, blank=True)
    zona_ubucacion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed             = False
        db_table            = 'auxiliares\".\"plantel'
        verbose_name        = 'plantel'
        verbose_name_plural = 'planteles'

    def __str__(self):
        return self.cod_plantel
