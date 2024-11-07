from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional

class EstudianteSchemaIn(Schema):
    director_id: int
    nivel_id: int
    cantidad_femenino: int  
    cantidad_masculino: int

class EstudianteSchemaOut(Schema):
    id: int
    director_id: int
    nivel_id: int
    cantidad_femenino: int  
    cantidad_masculino: int



