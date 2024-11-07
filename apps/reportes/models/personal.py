from django.db import models
from datetime import datetime

from apps.auxiliares.models.clasificacion import Clasificacion
from apps.cuenta.models import User

hoy = datetime.now().day
mes = datetime.now().month
anio= datetime.now().year

class Personal(models.Model):
    director            =   models.ForeignKey(User,                     on_delete = models.PROTECT,                             )
    clasificacion       =   models.ForeignKey(Clasificacion,             on_delete = models.PROTECT,                            )
    cantidad_femenino   =   models.IntegerField('Femenino',             blank=True, null=True                                   )
    cantidad_masculino  =   models.IntegerField('Masculino',            blank=True, null=True                                   )
    total               =   models.IntegerField('Total',                blank=True, null=True                                   )
    dia                 =   models.IntegerField('Día')
    mes                 =   models.IntegerField('Mes')
    anio                =   models.IntegerField('Año')
    
    def save(self, *args, **kwargs): 
        self.total = self.cantidad_femenino + self.cantidad_masculino
        self.dia = hoy
        self.mes = mes
        self.anio = anio
        super(Personal, self).save(*args, **kwargs)

    class Meta:
        managed             = False
        unique_together     = ('director', 'clasificacion','dia', 'mes', 'anio')
        db_table            = 'reportes\".\"personal'
        verbose_name        = 'Personal'
        verbose_name_plural = 'Personales'
        
    def __str__(self):
        return f'{self.director} {self.clasificacion} {self.cantidad_femenino} {self.cantidad_masculino} {self.total}'
