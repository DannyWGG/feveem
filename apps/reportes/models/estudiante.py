from django.db import models
from datetime import datetime

from apps.auxiliares.models.nivel import Nivel
from apps.cuenta.models import User

hoy = datetime.now().day
mes = datetime.now().month
anio= datetime.now().year

class Estudiante(models.Model):
    director            =   models.ForeignKey(User,                     on_delete = models.PROTECT)
    nivel               =   models.ForeignKey(Nivel,                    on_delete = models.PROTECT)
    cantidad_femenino   =   models.IntegerField('Femenino',             blank=True, null= True,                         )
    cantidad_masculino  =   models.IntegerField('Masculino',            blank=True, null= True,                         )
    total               =   models.IntegerField('Total',                blank=True, null= True,                         )
    dia                 =   models.IntegerField('Día')
    mes                 =   models.IntegerField('Mes')
    anio                =   models.IntegerField('Año')
    
    def save(self, *args, **kwargs): 
        self.total = self.cantidad_femenino + self.cantidad_masculino
        self.dia = hoy
        self.mes = mes
        self.anio = anio
        super(Estudiante, self).save(*args, **kwargs)
    
    class Meta:
        managed             = False
        unique_together     = ('director', 'nivel','dia', 'mes', 'anio')
        db_table            = 'reportes\".\"estudiante'
        verbose_name        = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f'{self.nivel.descripcion} {self.cantidad_femenino} {self.cantidad_masculino} {self.total}'
