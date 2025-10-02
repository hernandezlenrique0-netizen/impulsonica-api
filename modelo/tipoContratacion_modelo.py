from pydantic import BaseModel

class TipoContratacion(BaseModel):
    Id: int
    Nombre: str

