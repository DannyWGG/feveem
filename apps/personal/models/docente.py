from django.db import models
from apps.auxiliares.models.plantel_consulta import  PlantelConsulta
from apps.auxiliares.models.areas_formacion  import  AreaFormacion
from apps.cuenta.models import User

class Docente(models.Model):
    V    =   'V'
    E    =   'E'

    ORIGEN  =   (
                    (V,  'V'),
                    (E,  'E'),
                )
    
    director                = models.ForeignKey(User,                     on_delete = models.PROTECT)
    origen                  = models.CharField('Origen', max_length =   1,   choices = ORIGEN)
    cedula                  = models.CharField(max_length=20,    unique=True)
    codigo_plantel          = models.CharField('Codigo Plantel',            max_length = 10,    blank = True, null = True                  )    
    tipo_cargo              = models.CharField(max_length=255)
    nombres_apellidos       = models.CharField(max_length=255)
    numero_cuenta           = models.IntegerField(blank = True, null = True)

    class Meta:
        managed             = True
        db_table            = 'personal\".\"docente'
        verbose_name        = 'Docente'
        verbose_name_plural = 'Docentes'
        
    def __str__(self):
        return f'{self.nombres_apellidos} {self.codigo_plantel}'


class AreaPersonal(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='areas_personal')
    area_formacion = models.ForeignKey(AreaFormacion, on_delete=models.CASCADE, related_name='personal_areas')

    class Meta:
        managed             = True
        db_table            = 'personal\".\"area_personal'
        verbose_name        = 'Area Personal'
        verbose_name_plural = 'Areas Personal'

    def __str__(self):
        return f"Docente: {self.docente}, Área formacion: {self.area_formacion}"