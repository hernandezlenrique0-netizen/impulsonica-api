from pydantic import BaseModel
from typing import Optional
from datetime import date

class Empleos(BaseModel):
    Id: int
    Nombre: str
    Descripción: str
    Ubicación: str
    Salario: str
    FechaPublicación: date
    FechaExpiración: date
    EmpresaId: int
    DepartamentoId: int


