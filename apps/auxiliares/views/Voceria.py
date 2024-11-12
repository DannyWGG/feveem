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
@router.get("/listar", tags=tag, response=List[VoceriaSchemaOut], auth=JWTAuth())
def listar_vocerias(request):
    """ Endpoint para listar los tipos de vocerias """

    return Voceria.objects.all()

# Endpoint para crear una voceria
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
