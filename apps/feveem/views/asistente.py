from ninja                          import Router
from ninja.errors                   import HttpError
from apps.feveem.models.asistente   import Asistente
from typing                         import List
from apps.feveem.schemes.asistente  import AsistenteSchemaIn, AsistenteSchemaOut
from configuracion.schemes          import ErrorSchema
from configuracion.schemes          import SucessSchema

tag = ['asistentes']
router = Router()

# Endpoint para listar todas las áreas de personal
@router.get("/ver", tags=tag, response=List[AsistenteSchemaOut])
def listar_asistentes(request):
    return Asistente.objects.all()

@router.get("/buscar", tags=tag, response=AsistenteSchemaOut)

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
@router.post("/crear", tags=tag, response=AsistenteSchemaIn)
def crear_asistente(request, data: AsistenteSchemaIn):
    asistente = Asistente.objects.create(**data.dict())
    return asistente


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