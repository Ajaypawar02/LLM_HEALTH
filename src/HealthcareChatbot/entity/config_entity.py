from dataclasses import dataclass
from pathlib import Path
from typing import List
from pydantic import BaseModel

@dataclass(frozen=True)
class DataBaseConfig:
    """Database configuration"""

    host: str
    user: str
    password: str
    database: str

@dataclass(frozen=True)
class ModelConfig:
    """Model configuration"""

    temperature: float
    model_name: str

class APIPARAMETERS(BaseModel):
    """API configuration"""

    recipe_name: str
    ingredients: List
    ingredients_to_replace: List
    ingredient_preparation: List
