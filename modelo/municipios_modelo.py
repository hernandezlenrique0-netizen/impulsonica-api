# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Municipios que hereda de BaseModel
class Municipios(BaseModel):
    Id: int             # Identificador único del municipio
    Nombre: str         # Nombre del municipio (por ejemplo: "Tipitapa", "Estelí")
    DepartamentoId: int # ID del departamento al que pertenece este municipio
