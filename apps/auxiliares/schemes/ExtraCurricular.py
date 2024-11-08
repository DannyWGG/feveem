from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional

class ExtraCurricularSchemaIn(Schema):
    
    descripcion: str
    estatus: bool

class ExtraCurricularSchemaOut(Schema):
    
    id: int
    descripcion: str
    estatus: bool






