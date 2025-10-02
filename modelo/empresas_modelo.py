from pydantic import BaseModel

class Empresas(BaseModel):
    Id: int
    Nombres: str
    Usuario: str
    Contraseña: str
    Descripcion: str
    Actividad: str
    Email: str
    Telefono: str
    MunicipioId: int
    DepartamentoId: int

