from ninja                          import Router
from ninja.errors                   import HttpError
from apps.personal.models.docente   import Docente, AreaPersonal
from apps.auxiliares.models.areas_formacion   import AreaFormacion
from typing                         import List
from apps.personal.schemes.docente  import AreaPersonalSchema, MultipleAreaPersonalCreateSchema
from configuracion.schemes      import ErrorSchema
from configuracion.schemes      import SucessSchema

tag = ['areas_personal']
router = Router()

# Endpoint para listar todas las áreas de personal
@router.get("/ver", tags=tag, response=List[AreaPersonalSchema])
def listar_areas_personal(request):
    return AreaPersonal.objects.all()

# Endpoint para obtener un área de personal específico por su ID
@router.get("/listar/{area_id}", tags=tag, response=AreaPersonalSchema)
def ver_area_personal(request, area_id: int):
    try:
        area_personal = AreaPersonal.objects.get(id=area_id)
        return area_personal
    except AreaPersonal.DoesNotExist:
        raise HttpError(404, "Área personal no encontrada")

# Endpoint para crear un área de personal
# @router.post("/areas_personal", tags=tag, response=AreaPersonalSchema)
# def crear_area_personal(request, data: AreaPersonalSchema):
#     area_personal = AreaPersonal.objects.create(**data.dict())
#     return area_personal


@router.post('/create', tags=tag, response = {201: SucessSchema, 400: ErrorSchema})
def create_materia(request, payload: List[AreaPersonalSchema]):
    try:
        areaspersonal = [
            AreaPersonal(
                docente_id=item.docente_id,
                area_formacion_id=item.area_formacion_id,
            )
            for item in payload
        ]
        AreaPersonal.objects.bulk_create(areaspersonal)
        return 201, {"message": "Operacion Exitosa"}
    except Exception as e:
        return 400, {"message": f"Operacion Fallida: {str(e)}"}
