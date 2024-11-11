from django.db import models
from apps.cuenta.models import User
from apps.auxiliares.models.Voceria import Voceria
from apps.auxiliares.models.ExtraCurricular import ActividadExtraCurricular
from apps.cuenta.models import User

import os
import requests
import json
from decouple import config
from requests.exceptions import RequestException

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
    fecha_nacimiento = models.CharField(max_length=10, blank=True, null=True)
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
    identificador = models.CharField(max_length=100, unique=True, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):

        headers     = {'Content-Type': 'application/json'}

        try:
            response_data = requests.get(f"https://visitantes.me.gob.ve/saime/{self.origen}/{self.cedula}/", headers=headers, verify=False)
            if response_data.status_code == 200:
                
                data = response_data.json()
                self.identificador = self.origen + str(self.cedula)

                self.primer_nombre = data.get('primer_nombre', '')
                self.segundo_nombre = data.get('segundo_nombre', '')
                self.primer_apellido = data.get('primer_apellido', '')
                self.segundo_apellido = data.get('segundo_apellido', '')
                self.fecha_nacimiento = data.get('fecha_nacimiento', '')

                super(Asistente, self).save(*args, **kwargs)

        except (ValueError, RequestException) as e:
            print(f"Error al consultar de Saime: {str(e)}")
            

    class Meta:
        managed             = True
        db_table            = 'feveem\".\"asistente'
        verbose_name        = 'Vocero'
        verbose_name_plural = 'Voceros'
        unique_together     = ('cedula', 'origen',)
        
    def __str__(self):
        return f'{self.primer_nombre} {self.primer_apellido}'
