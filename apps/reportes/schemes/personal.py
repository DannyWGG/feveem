from ninja.orm import ModelSchema  
from ninja import Schema
from typing import List, Optional

class PersonalSchemaIn(Schema):
    director_id: int
    clasificacion_id: int
    cantidad_femenino: int  
    cantidad_masculino: int

class PersonalSchemaOut(Schema):
    id: int
    director_id: int
    clasificacion_id: int
    cantidad_femenino: int  
    cantidad_masculino: int



