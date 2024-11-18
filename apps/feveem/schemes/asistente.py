from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional


# Subesquemas
class SubSchemaExtraCurricularSchemaOut(Schema):
    descripcion: str

class SubSchemaVoceriaSchemaOut(Schema):
    id: int
    descripcion: str
    estatus: bool


class AsistenteSchemaIn(Schema):
    primer_nombre: Optional[str]
    segundo_nombre: Optional[str]
    primer_apellido: Optional[str]
    segundo_apellido: Optional[str]
    origen: str
    cedula: int
    fecha_nacimiento: Optional[str]
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
    identificador: Optional[str]
    usuario_id: int

class AsistenteSchemaOut(Schema):
    id: int
    primer_nombre: Optional[str]
    segundo_nombre: Optional[str]
    primer_apellido: Optional[str]
    segundo_apellido: Optional[str]
    origen: str
    cedula: int
    fecha_nacimiento: Optional[str]
    cod_plantel: str
    institucion_educativa: str
    anio_curso: str
    voceria: Optional[SubSchemaVoceriaSchemaOut]
    municipio: Optional[str]
    estado: Optional[str]
    numero_telefono: Optional[str]
    correo: Optional[str]
    usuario_instagram: Optional[str]
    usuario_tiktok: Optional[str]
    extra_curricular: Optional[SubSchemaExtraCurricularSchemaOut]
    identificador: Optional[str]
    usuario_id: int

class VoceriaEstadoCountSchema(Schema):
    estado: str
    voceria__descripcion: str
    total: int

class ContadorResponseSchema(Schema):
    resultados: List[VoceriaEstadoCountSchema]

class RegistroCountSchema(Schema):

    directores_count: int
    asistente_count: int
    voceria_count: int
    extracurricular_count: int
