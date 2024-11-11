from ninja import Schema
from typing import Optional

class PlantelSchemaIn(Schema):
    estado: Optional[str] = None
    periodo_escolar: Optional[str] = None
    municipio: Optional[str] = None
    parroquia: Optional[str] = None
    cod_plantel: Optional[str] = None
    nombre_plantel: Optional[str] = None
    tipo_dependencia: Optional[str] = None
    modalidad_principal: Optional[str] = None
    estatus_plantel: Optional[str] = None
    nivel_principal: Optional[str] = None
    zona_ubicacion: Optional[str] = None
    
    maternal_masculino: Optional[int] = None
    maternal_femenino: Optional[int] = None
    prescolar_masculino: Optional[int] = None
    prescolar_femenino: Optional[int] = None
    primaria_masculino: Optional[int] = None
    primaria_femenino: Optional[int] = None
    media_masculino: Optional[int] = None
    media_femenino: Optional[int] = None
    media_general_masculino: Optional[int] = None
    media_general_femenino: Optional[int] = None
    tecnica_masculino: Optional[int] = None
    tecnica_femenino: Optional[int] = None
    adulto_masculino: Optional[int] = None
    adulto_femenino: Optional[int] = None
    especial_masculino: Optional[int] = None
    especial_femenino: Optional[int] = None
    
    total: Optional[int] = None
    
    director_nombre: Optional[str] = None
    director_apellido: Optional[str] = None
    tipo_documento: Optional[str] = None
    documento_identidad: Optional[str] = None
    telefono_director: Optional[str] = None
    telefono_movil_director: Optional[str] = None
    correo: Optional[str] = None
    twitter: Optional[str] = None
    direccion: Optional[str] = None
    
    peridoescolar: Optional[int] = None
    zona_ubucacion: Optional[str] = None

class PlantelSchemaOut(PlantelSchemaIn):
    id: int
    
