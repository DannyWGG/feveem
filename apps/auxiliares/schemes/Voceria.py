from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional

class VoceriaSchemaIn(Schema):
    
    descripcion: str
    estatus: bool

class VoceriaSchemaOut(Schema):
    
    id: int
    descripcion: str
    estatus: bool






