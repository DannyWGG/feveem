from ninja import Router
from ninja.errors import HttpError
from apps.auxiliares.models.Voceria import Voceria
from typing                         import List
from apps.auxiliares.schemes.Voceria  import VoceriaSchemaIn, VoceriaSchemaOut
from configuracion.schemes      import ErrorSchema
from configuracion.schemes      import SucessSchema

from ninja_jwt.authentication import JWTAuth

tag = ['Voceria']
router = Router()

# Endpoint para listar todas las áreas de personal
@router.get('/ver/', tags=tag, response=List[VoceriaSchemaOut], auth=JWTAuth())
def listar_docentes(request):
    voceria = Voceria.objects.filter(estatus=True)
    return voceria

# Endpoint para obtener un área de personal específico por su ID
@router.get("/listar/{id}", tags=tag, response=VoceriaSchemaOut, auth=JWTAuth())
def ver_area_personal(request, area_id: int):
    try:
        voceria = Voceria.objects.get(id=area_id)
        return voceria
    except Voceria.DoesNotExist:
        raise HttpError(404, "Opción no encontrada")

# Endpoint para crear un área de personal
@router.post("/crear", tags=tag, response=VoceriaSchemaIn, auth=JWTAuth())
def crear_area_personal(request, data: VoceriaSchemaIn):
    voceria = Voceria.objects.create(**data.dict())
    return voceria


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
