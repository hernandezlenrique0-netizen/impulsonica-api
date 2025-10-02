from pydantic import BaseModel
from typing import Optional
from datetime import date

class Postulaciones(BaseModel):
    Id: int
    CandidatoId: int
    EmpleoId: int
    FechaPublicación: date
    EstadoPostulación: bool

