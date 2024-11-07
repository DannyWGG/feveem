from ninja import Router
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth
from django.db                          import IntegrityError

from apps.reportes.models.estudiante import Estudiante
from apps.auxiliares.models.nivel import Nivel
from apps.cuenta.models import User
from configuracion.schemes      import ErrorSchema
from configuracion.schemes      import SucessSchema

from typing import List
from apps.reportes.schemes.estudiante import EstudianteSchemaIn, EstudianteSchemaOut
from django.shortcuts import get_object_or_404

tag = ['estudiante']
router = Router()

@router.post("/create", tags=tag, response = {201: SucessSchema, 400: ErrorSchema})
def crear_estudiante(request, data: EstudianteSchemaIn):
    try:
        # Verificar si el nivel existe
        director = User.objects.get(id=data.director_id)
        nivel = Nivel.objects.get(id=data.nivel_id)
        
        # Crear el estudiante si el nivel es válido
        estudiante = Estudiante.objects.create(**data.dict())
        return 201, {"message": "Operacion Exitosa"}
    except User.DoesNotExist:
        raise HttpError(404, "El director no existe")
    except Nivel.DoesNotExist:
        raise HttpError(404, "El nivel no existe")
    except Estudiante.DoesNotExist:
        raise HttpError(404, "Error al crear el estudiante")
    except IntegrityError:
        raise HttpError(400, "Error en los datos")
