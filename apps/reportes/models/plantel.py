from django.db import models

class Plantel(models.Model):
    nombre      =   models.CharField(               max_length=255,     blank=True,    null=True                  )
    codigo      =   models.CharField('Código',      max_length=100,     blank=True,    null=True, unique = True   )
    direccion   =   models.CharField('Dirección',   max_length=255,     blank=True,    null=True                  )
    telefono    =   models.CharField('Teléfono',    blank=True,         null=True                                 )
    
    class Meta:
        managed             = True
        db_table            = 'reportes\".\"plantel'
        verbose_name        = 'Plantel'
        verbose_name_plural = 'Planteles'
        
    def __str__(self):
        return f'{self.nombre} {self.codigo} {self.direccion} {self.telefono}'
