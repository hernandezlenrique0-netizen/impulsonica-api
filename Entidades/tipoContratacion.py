# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos TipoContratacion desde el archivo correspondiente
from modelo.tipoContratacion_modelo import TipoContratacion

# Definimos una clase que encapsula las rutas relacionadas con el recurso "TipoContratacion"
class TipoContratacionAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un tipo de contratación de ejemplo (simula una base de datos en memoria)
        self.tipoContratacion = [
            TipoContratacion(
                Id=1,
                Nombre="Tiempo Completo"  # Nombre del tipo de contratación
            )
        ]

        # Registramos la ruta GET "/Tcontratación" que llama al metodo obtener_Tcontrataciones
        self.router.get("/Tcontratación")(self.obtener_Tcontrataciones)

        # Registramos la ruta POST "/Tcontratación" que llama al metodo creater_Tcontrataciones
        self.router.post("/Tcontratación")(self.creater_Tcontrataciones)

    # Metodo que se ejecuta cuando se hace una petición GET a "/Tcontratación"
    def obtener_Tcontrataciones(self):
        # Devuelve la lista de tipos de contratación almacenados
        return self.tipoContratacion

    # Metodo que se ejecuta cuando se hace una petición POST a "/Tcontratación"
    def creater_Tcontrataciones(self, tcontratacion: TipoContratacion):
        # Agrega el nuevo tipo de contratación a la lista
        self.tipoContratacion.append(tcontratacion)

        # Devuelve un mensaje de confirmación junto con el tipo de contratación agregado
        return {
            "mensaje ": "tipo de contratación agregada con éxito",
            "tipoContratacion": tcontratacion
        }
