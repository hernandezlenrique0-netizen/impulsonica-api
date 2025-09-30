# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Candidatos que hereda de BaseModel
class Candidatos(BaseModel):
    Id: int  # Identificador único del candidato
    Usuario: str  # Nombre de usuario para iniciar sesión
    Contraseña: str  # Contraseña del candidato
    Nombres: str  # Nombres del candidato
    Apellidos: str  # Apellidos del candidato
    Genero: str  # Género del candidato (por ejemplo: "M" o "F")
    Email: str  # Correo electrónico del candidato
    Telefono1: str  # Primer número de teléfono de contacto
    Telefono2: str  # Segundo número de teléfono de contacto
    MunicipioId: int  # ID del municipio donde reside el candidato
    DepartamentoId: int  # ID del departamento correspondiente
