# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Empresas desde el archivo correspondiente
from modelo.empresas_modelo import Empresas

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Empresas"
class EmpresasAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con una empresa de ejemplo (simula una base de datos en memoria)
        self.empresas = [
            Empresas(
                Id=1,
                Nombres="Banco Lafise",  # Nombre de la empresa
                Usuario="lafise_admin",  # Usuario de acceso para la empresa
                Contraseña="LafiseSecure2025!",  # Contraseña de acceso
                Descripcion="Empresa financiera con presencia nacional",  # Breve descripción de la empresa
                Actividad="Servicios bancarios",  # Actividad principal de la empresa
                Email="contacto@lafise.com",  # Correo electrónico de contacto
                Telefono="82547890",  # Teléfono de contacto
                MunicipioId=5,  # ID del municipio donde se ubica la empresa
                DepartamentoId=2  # ID del departamento correspondiente
            )
        ]

        # Registramos la ruta GET "/empresas" que llama al metodo obtener_empresas
        self.router.get("/empresas")(self.obtener_empresas)

        # Registramos la ruta POST "/empresas" que llama al metodo creater_empresas
        self.router.post("/empresas")(self.creater_empresas)

    # Metodo que se ejecuta cuando se hace una petición GET a "/empresas"
    def obtener_empresas(self):
        # Devuelve la lista de empresas almacenadas
        return self.empresas

    # Metodo que se ejecuta cuando se hace una petición POST a "/empresas"
    def creater_empresas(self, empresas: Empresas):
        # Agrega la nueva empresa a la lista
        self.empresas.append(empresas)

        # Devuelve un mensaje de confirmación junto con la empresa agregada
        return {
            "mensaje ": "empresa agregada con exito",
            "empresas": empresas
        }
