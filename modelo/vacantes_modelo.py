# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Vacantes que hereda de BaseModel
class Vacantes(BaseModel):
    Id: int  # Identificador único de la vacante
    Nombre: str  # Título general de la vacante (por ejemplo: "Se solicita un programador")
    CargoSolicitado: str  # Cargo específico que se está buscando (por ejemplo: "Programador web")
    NombreEmpresa: str  # Nombre de la empresa que publica la vacante
    AreaEmpresa: str  # Área o sector de la empresa (por ejemplo: "Tecnología", "Finanzas")
    TipoContratacionId: int  # ID del tipo de contratación (relación con tabla TipoContratacion)
    NivelExperiencia: str  # Nivel de experiencia requerido (por ejemplo: "1 año", "Senior")
    DepartementoId: int  # ID del departamento donde se ubica la vacante
    MunicipioId: int  # ID del municipio correspondiente
    Email: str  # Correo electrónico de contacto para postulaciones
    Telefono: str  # Número de teléfono de contacto
    Expira: str  # Tiempo de vigencia de la vacante (por ejemplo: "1 mes", "30 días")
    Descripcion: str  # Descripción detallada del puesto y sus funciones
    Requisitos: str  # Requisitos que debe cumplir el postulante (por ejemplo: "Currículum completo")
    EmpleosId: int  # ID del empleo relacionado (relación con tabla Empleos)

