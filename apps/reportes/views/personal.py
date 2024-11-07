from ninja import Router
from ninja.errors import HttpError
from django.db                          import IntegrityError

from apps.reportes.models.personal import Personal
from apps.auxiliares.models.clasificacion import Clasificacion
from apps.cuenta.models import User
from configuracion.schemes      import ErrorSchema
from configuracion.schemes      import SucessSchema
from ninja_jwt.authentication import JWTAuth

from typing import List
from apps.reportes.schemes.personal import PersonalSchemaIn
from django.shortcuts import get_object_or_404

tag = ['personal']
router = Router()

@router.post("/create", tags=tag, response = {201: SucessSchema, 400: ErrorSchema})
def crear_personal(request, data: PersonalSchemaIn):
    try:
        # Verificar si el nivel existe
        director = User.objects.get(id=data.director_id)
        clasificacion = Clasificacion.objects.get(id=data.clasificacion_id)
        
        # Crear el personal si el nivel es válido
        personal = Personal.objects.create(**data.dict())
        return 201, {"message": "Operacion Exitosa"}
    except User.DoesNotExist:
        raise HttpError(404, "El director no existe")
    except Clasificacion.DoesNotExist:
        raise HttpError(404, "La clasificación no existe")
    except Personal.DoesNotExist:
        raise HttpError(404, "Error al crear el personal")
    except IntegrityError:
        raise HttpError(400, "Error en los datos")

