from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional


class AsistenteSchemaIn(Schema):

    primer_nombre: Optional[str]
    segundo_nombre: Optional[str]
    primer_apellido: Optional[str]
    segundo_apellido: Optional[str]
    origen: str
    cedula: int
    fecha_nacimiento: str
    cod_plantel: str
    institucion_educativa: str
    anio_curso: str
    voceria_id: int
    municipio: Optional[str]
    estado: Optional[str]
    numero_telefono: Optional[str]
    correo: Optional[str]
    usuario_instagram: Optional[str]
    usuario_tiktok: Optional[str]
    extra_curricular_id: int
    identificador: str
    usuario_id: int

class AsistenteSchemaOut(Schema):
    
    id: int
    primer_nombre: Optional[str]
    segundo_nombre: Optional[str]
    primer_apellido: Optional[str]
    segundo_apellido: Optional[str]
    origen: str
    cedula: int
    fecha_nacimiento: str
    cod_plantel: str
    institucion_educativa: str
    anio_curso: str
    voceria_id: int
    municipio: Optional[str]
    estado: Optional[str]
    numero_telefono: Optional[str]
    correo: Optional[str]
    usuario_instagram: Optional[str]
    usuario_tiktok: Optional[str]
    extra_curricular_id: int
    identificador: str
    usuario_id: int