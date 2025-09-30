# Importamos APIRouter desde FastAPI para crear rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Administrador desde otro archivo
from modelo.administrador_modelo import Administrador

# Definimos una clase que encapsula las rutas relacionadas con "Administrador"
class AdministradorAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un administrador de ejemplo (simula una base de datos en memoria)
        self.administrador = [
            Administrador(
                Id=2,
                Usuario="mariolopez2025",
                Contrasenia="MarioSecurePass!",
                Nombres="Mario",
                Apellidos="López",
                Telefono="87451236",
                MunicipioId=4,
                DepartamentoId=2
            )
        ]

        #Registramos la ruta GET "/administrador" que llama al metodo obtener_administrador
        self.router.get("/administrador")(self.obtener_administrador)

        # Registramos la ruta POST "/administrador" que llama al metodo creater_administrador
        self.router.post("/administrador")(self.creater_administrador)

    # Metodo que se ejecuta cuando se hace una petición GET a "/administrador"
    def obtener_administrador(self):
        print("🚀 Se llamó a /administrador")  # Mensaje de depuración en consola
        return self.administrador  # Devuelve la lista de administradores

    # Metodo que se ejecuta cuando se hace una petición POST a "/administrador"
    def creater_administrador(self, administrador: Administrador):
        self.administrador.append(administrador)  # Agrega el nuevo administrador a la lista
        return {
            "mensaje ": " administrador agregado con exito",  # Mensaje de confirmación
            "administrador": administrador  # Devuelve el administrador recién agregado
        }




