from ninja                              import Router
from ninja.errors                       import HttpError
from apps.auxiliares.models.plantel     import Plantel
from typing                             import List
from apps.auxiliares.schemes.plantel    import PlantelSchemaIn, PlantelSchemaOut
from configuracion.schemes              import ErrorSchema
from configuracion.schemes              import SucessSchema
from ninja_jwt.authentication           import JWTAuth

tag = ['directores']
router = Router()

# # Endpoint para listar todas las áreas de personal
# @router.get("/ver", tags=tag, response=List[AsistenteSchemaOut], auth=JWTAuth())
# def listar_asistentes(request):
#     return Asistente.objects.all()


# # Endpoint para listar todos los asistente
# @router.get('/filtro/{usuario_id}', tags=tag, response=List[AsistenteSchemaOut], auth=JWTAuth())
# def filtro(request, usuario_id:int ):
#     usuario = Asistente.objects.filter(usuario_id=usuario_id)
#     return usuario


@router.get("/buscar/{origen}/{cedula}", tags=tag, response=PlantelSchemaOut)
def consultar_director(request, origen: str, cedula: int):
    """
    description="Busca un director específico por su origen y cédula. "
                "Si el director no se encuentra, se lanza un error 404.",
    """    
    planteles = Plantel.objects.filter(tipo_documento=origen, documento_identidad=cedula)
    if planteles.exists():
        # Si hay más de un registro, puedes manejarlo según sea necesario (e.g., tomar el primero)
        plantelSchemaOut = planteles.first()  # Devuelve el primer registro encontrado
        return plantelSchemaOut
    else:
        raise HttpError(404, "El director no existe")


@router.get("/consultar/{cod_plantel}", tags=tag, response=PlantelSchemaOut)
def consultar_plantel(request, cod_plantel: str):
    """
    description="Busca un plantel específico por su codigo de plantel. "
                "Si el plantel no se encuentra, se lanza un error 404.",
    """    
    planteles = Plantel.objects.filter(cod_plantel=cod_plantel)
    if planteles.exists():
        # Si hay más de un registro, puedes manejarlo según sea necesario (e.g., tomar el primero)
        plantelSchemaOut = planteles.first()  # Devuelve el primer registro encontrado
        return plantelSchemaOut
    else:
        raise HttpError(404, "El plantel no existe")


## Endpoint para obtener un área de personal específico por su ID
#@router.get("/listar/{area_id}", tags=tag, response=AreaPersonalSchema)
#def ver_area_personal(request, area_id: int):
#    try:
#        area_personal = AreaPersonal.objects.get(id=area_id)
#        return area_personal
#    except AreaPersonal.DoesNotExist:
#        raise HttpError(404, "Área personal no encontrada")

# Endpoint para crear un área de personal
# @router.post("/crear", tags=tag, response=AsistenteSchemaIn, auth=JWTAuth())
# def crear_asistente(request, data: AsistenteSchemaIn):
#     asistente = Asistente.objects.create(**data.dict())
#     return asistente


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