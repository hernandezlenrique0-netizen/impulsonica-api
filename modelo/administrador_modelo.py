from pydantic import BaseModel

class Administrador(BaseModel):
    Id: int
    Usuario: str
    Contrasenia: str
    Nombres: str
    Apellidos: str
    Telefono: str
    MunicipioId: int
    DepartamentoId: int

