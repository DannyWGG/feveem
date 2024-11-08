from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional


class DocenteSchemaIn(Schema):
    director_id: int
    origen: str
    cedula: str
    codigo_plantel: str  
    tipo_cargo: str
    nombres_apellidos: str
    numero_cuenta: Optional[int]

class DocenteSchemaOut(Schema):
    id: int
    director_id: int
    origen: str
    cedula: str
    codigo_plantel: str  
    tipo_cargo: str
    nombres_apellidos: str
    numero_cuenta: Optional[int]

class AreaPersonalSchema(Schema):
     docente_id: int  
     area_formacion_id: int  

class MultipleAreaPersonalCreateSchema(Schema):
    areas: List[AreaPersonalSchema]  # Lista de áreas de personal a crear





