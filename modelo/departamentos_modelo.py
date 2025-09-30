# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Departamentos que hereda de BaseModel
class Departamentos(BaseModel):
    Id: int       # Identificador único del departamento (por ejemplo: 1 para Managua)
    Nombre: str   # Nombre del departamento (por ejemplo: "Managua", "León", "Granada")
