# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Administrador que hereda de BaseModel
class Administrador(BaseModel):
    Id: int  # Identificador único del administrador
    Usuario: str  # Nombre de usuario para iniciar sesión
    Contrasenia: str  # Contraseña del administrador
    Nombres: str  # Nombres del administrador
    Apellidos: str  # Apellidos del administrador
    Telefono: str  # Número de teléfono de contacto
    MunicipioId: int  # ID del municipio donde reside o trabaja el administrador
    DepartamentoId: int  # ID del departamento correspondiente
