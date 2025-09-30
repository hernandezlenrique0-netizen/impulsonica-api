# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Importamos Optional por si queremos campos opcionales en el futuro (aunque aquí no se usa)
from typing import Optional

# Importamos date para trabajar con fechas específicas
from datetime import date

# Definimos la clase Postulaciones que hereda de BaseModel
class Postulaciones(BaseModel):
    Id: int  # Identificador único de la postulación
    CandidatoId: int  # ID del candidato que realiza la postulación
    EmpleoId: int  # ID del empleo al que se postula
    FechaPublicación: date  # Fecha en que se realizó la postulación
    EstadoPostulación: bool  # Estado de la postulación (True = activa, False = inactiva o rechazada)
