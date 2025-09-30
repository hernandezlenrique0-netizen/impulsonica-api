# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Empresas que hereda de BaseModel
class Empresas(BaseModel):
    Id: int               # Identificador único de la empresa
    Nombres: str          # Nombre oficial de la empresa
    Usuario: str          # Usuario para que la empresa acceda al sistema
    Contraseña: str       # Contraseña de acceso para la empresa
    Descripcion: str      # Breve descripción de la empresa (por ejemplo: "Empresa financiera con presencia nacional")
    Actividad: str        # Actividad principal de la empresa (por ejemplo: "Servicios bancarios", "Tecnología")
    Email: str            # Correo electrónico de contacto de la empresa
    Telefono: str         # Número de teléfono de contacto
    MunicipioId: int      # ID del municipio donde se ubica la empresa
    DepartamentoId: int   # ID del departamento correspondiente
