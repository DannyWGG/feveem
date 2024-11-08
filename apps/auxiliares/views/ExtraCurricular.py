from ninja import Router
from ninja.errors import HttpError
from apps.auxiliares.models.ExtraCurricular import ActividadExtraCurricular
from typing import List
from apps.auxiliares.schemes.ExtraCurricular import ExtraCurricularSchemaIn, ExtraCurricularSchemaOut

from ninja_jwt.authentication import JWTAuth

tag = ['Actividad Extra Curricular']
router = Router()

# Endpoint para listar todas las áreas de personal
#@router.get("/ver", tags=tag, response=List[ExtraCurricularSchemaOut])
#def listar_areas_personal(request):
#    return ActividadExtraCurricular.objects.all()

# Endpoint para listar todos los docentes con estatus true
@router.get('/ver/', tags=tag, response=List[ExtraCurricularSchemaOut], auth=JWTAuth())
def listar_docentes(request):
    curricular = ActividadExtraCurricular.objects.filter(estatus=True)
    return curricular


# Endpoint para obtener un docente específico por su ID
@router.get("/filtro/{id}",  tags=tag, response=ExtraCurricularSchemaOut, auth=JWTAuth())
def ver_docente(request, id: int):
    try:
        curricular = ActividadExtraCurricular.objects.get(id=id, estatus=True)
        return curricular
    except ActividadExtraCurricular.DoesNotExist:
        raise HttpError(404, "Opción no encontrada")

# Endpoint para crear un docente
@router.post("/crear", tags=tag, response=ExtraCurricularSchemaIn, auth=JWTAuth())
def crear_docente(request, data: ExtraCurricularSchemaIn):
    curricular = ActividadExtraCurricular.objects.create(**data.dict())
    return curricular