# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Importamos Optional por si queremos campos opcionales en el futuro (aunque aquí no se usa)
from typing import Optional

# Importamos date para trabajar con fechas específicas
from datetime import date

# Definimos la clase Empleos que hereda de BaseModel
class Empleos(BaseModel):
    Id: int  # Identificador único del empleo
    Nombre: str  # Título del empleo (por ejemplo: "Desarrollador Web Junior")
    Descripción: str  # Descripción general del puesto y responsabilidades
    Ubicación: str  # Ciudad o lugar donde se ofrece el empleo
    Salario: str  # Monto o rango salarial ofrecido (por ejemplo: "USD 800 mensuales")
    FechaPublicación: date  # Fecha en que se publicó la oferta de empleo
    FechaExpiración: date  # Fecha límite para aplicar a la oferta
    EmpresaId: int  # ID de la empresa que publica el empleo (relación con tabla Empresas)
    DepartamentoId: int  # ID del departamento donde se ubica el empleo (relación con tabla Departamentos)

