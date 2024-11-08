from ninja import Router
from ninja.errors import HttpError
from apps.personal.models.docente import Docente
from typing import List
from apps.personal.schemes.docente import DocenteSchemaIn, DocenteSchemaOut


tag = ['docente']
router = Router()

# Endpoint para listar todos los docentes
@router.get('/filtro/{director_id}', tags=tag, response=List[DocenteSchemaOut])
def filtro(request, director_id:int ):
    docente = Docente.objects.filter(director=director_id)
    return docente


# Endpoint para obtener un docente específico por su ID
@router.get("/listar/{cedula}",  tags=tag, response=DocenteSchemaOut)
def ver_docente(request, cedula: int):
    try:
        docente = Docente.objects.get(cedula=cedula)
        return docente
    except Docente.DoesNotExist:
        raise HttpError(404, "Docente no encontrado")

# Endpoint para crear un docente
@router.post("/create", tags=tag, response=DocenteSchemaIn)
def crear_docente(request, data: DocenteSchemaIn):
    docente = Docente.objects.create(**data.dict())
    return docente




