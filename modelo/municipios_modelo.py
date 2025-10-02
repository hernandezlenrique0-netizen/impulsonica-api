from pydantic import BaseModel

class Municipios(BaseModel):
    Id: int
    Nombre: str
    DepartamentoId: int

