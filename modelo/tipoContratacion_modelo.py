# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase TipoContratacion que hereda de BaseModel
class TipoContratacion(BaseModel):
    Id: int       # Identificador único del tipo de contratación (por ejemplo: 1 para "Tiempo Completo")
    Nombre: str   # Nombre del tipo de contratación (por ejemplo: "Tiempo Completo", "Medio Tiempo", "Contrato Temporal")
