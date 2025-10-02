from pydantic import BaseModel

class Vacantes(BaseModel):
    Id: int
    Nombre: str
    CargoSolicitado: str
    NombreEmpresa: str
    AreaEmpresa: str
    TipoContratacionId: int
    NivelExperiencia: str
    DepartementoId: int
    MunicipioId: int
    Email: str
    Telefono: str
    Expira: str
    Descripcion: str
    Requisitos: str
    EmpleosId: int


