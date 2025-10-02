from pydantic import BaseModel

class Candidatos(BaseModel):
    Id: int
    Usuario: str
    Contraseña: str
    Nombres: str
    Apellidos: str
    Genero: str
    Email: str
    Telefono1: str
    Telefono2: str
    MunicipioId: int
    DepartamentoId: int

