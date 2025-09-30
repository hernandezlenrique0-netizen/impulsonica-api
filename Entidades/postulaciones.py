# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Postulaciones desde el archivo correspondiente
from modelo.postulaciones_modelo import Postulaciones

# Importamos la clase date para manejar fechas
from datetime import date

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Postulaciones"
class PostulacionesAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con una postulación de ejemplo (simula una base de datos en memoria)
        self.postulaciones = [
            Postulaciones(
                Id=1,                          # ID único de la postulación
                CandidatoId=1,                 # ID del candidato que se postula
                EmpleoId=1,                    # ID del empleo al que se postula
                FechaPublicación=date(         # Fecha en que se realizó la postulación
                    year=2025, month=9, day=25
                ),
                EstadoPostulación=True         # Estado de la postulación (True = activa)
            )
        ]

        # Registramos la ruta GET "/postulaciones" que llama al metodo obtener_postulaciones
        self.router.get("/postulaciones")(self.obtener_postulaciones)

        # Registramos la ruta POST "/postulaciones" que llama al metodo creater_postulaciones
        self.router.post("/postulaciones")(self.creater_postulaciones)

    # Metodo que se ejecuta cuando se hace una petición GET a "/postulaciones"
    def obtener_postulaciones(self):
        # Devuelve la lista de postulaciones almacenadas
        return self.postulaciones

    # Metodo que se ejecuta cuando se hace una petición POST a "/postulaciones"
    def creater_postulaciones(self, postulaciones: Postulaciones):
        # Agrega la nueva postulación a la lista
        self.postulaciones.append(postulaciones)

        # Devuelve un mensaje de confirmación junto con la postulación agregada
        return {
            "mensaje ": " postulación agregada con exito",
            "postulción": postulaciones
        }
