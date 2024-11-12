from ninja                          import Router
from ninja.errors                   import HttpError
from apps.feveem.models.asistente   import Asistente
from typing                         import List
from apps.feveem.schemes.asistente  import AsistenteSchemaIn, AsistenteSchemaOut
from configuracion.schemes          import ErrorSchema
from configuracion.schemes          import SucessSchema

from ninja_jwt.authentication       import JWTAuth

import logging

tag = ['asistentes']
router = Router()

logger = logging.getLogger(__name__)

@router.get("/ver", tags=tag, response=List[AsistenteSchemaOut], auth=JWTAuth())
def listar_asistentes(request):
    return Asistente.objects.select_related('voceria', 'extra_curricular').all()

# Endpoint para listar todos los asistente
@router.get('/filtro/{usuario_id}', tags=tag, response=List[AsistenteSchemaOut], auth=JWTAuth())
def filtro(request, usuario_id:int ):
    usuario = Asistente.objects.filter(usuario_id=usuario_id)
    return usuario


@router.get("/buscar/{origen}/{cedula}", tags=tag, response=AsistenteSchemaOut, auth=JWTAuth())
def buscar_asistente(request, origen: str, cedula: int):
    """
    description="Busca un asistente específico por su origen y cédula. "
                "Si el asistente no se encuentra, se lanza un error 404.",

    """    
    try:
        asistente = Asistente.objects.get(origen=origen, cedula=cedula)
        return asistente
    except Asistente.DoesNotExist:
        raise HttpError(404, "Asistente no encontrado")

## Endpoint para obtener un área de personal específico por su ID
#@router.get("/listar/{area_id}", tags=tag, response=AreaPersonalSchema)
#def ver_area_personal(request, area_id: int):
#    try:
#        area_personal = AreaPersonal.objects.get(id=area_id)
#        return area_personal
#    except AreaPersonal.DoesNotExist:
#        raise HttpError(404, "Área personal no encontrada")

# Endpoint para crear un área de personal
@router.post("/crear", tags=tag, response={201: AsistenteSchemaOut, 400: str, 500: str}, auth=JWTAuth())
def crear_asistente(request, data: AsistenteSchemaIn):
    try:
        asistente = Asistente(**data.dict())
        asistente.save()  # Asegúrate de que esto se ejecute sin errores
        return 201, asistente  # Retorna el asistente creado con un código de estado 201
    except ValueError as e:
        logger.error(f"Error de valor: {str(e)}")
        raise HttpError(400, str(e))  # Retorna un mensaje de error específico
    except Exception as e:
        logger.error(f"Error inesperado al crear asistente: {str(e)}")
        raise HttpError(500, "Error interno del servidor. Por favor, inténtelo más tarde.")

#@router.post('/create', tags=tag, response = {201: SucessSchema, 400: ErrorSchema})
#def create_materia(request, payload: List[AreaPersonalSchema]):
#    try:
#        areaspersonal = [
#            AreaPersonal(
#                docente_id=item.docente_id,
#                area_formacion_id=item.area_formacion_id,
#            )
#            for item in payload
#        ]
#        AreaPersonal.objects.bulk_create(areaspersonal)
#        return 201, {"message": "Operacion Exitosa"}
#    except Exception as e:
#        return 400, {"message": f"Operacion Fallida: {str(e)}"}
#