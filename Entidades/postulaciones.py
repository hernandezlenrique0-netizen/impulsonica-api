# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Postulaciones desde el archivo correspondiente
from modelo.postulaciones_modelo import Postulaciones

# Importamos la clase date para manejar fechas
from datetime import date

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Postulaciones"
class PostulacionesAPI:
    def __init__(self):
        self.router = APIRouter()
        self.postulaciones = [
            Postulaciones(
                Id=1,                          # ID único de la postulación
                CandidatoId=1,                 # ID del candidato que se postula
                EmpleoId=1,                    # ID del empleo al que se postula
                FechaPublicación=date(2025, 9, 25),  # Fecha en que se realizó la postulación
                EstadoPostulación=True         # Estado de la postulación (True = activa)
            )
        ]

        # Registramos la ruta GET "/postulaciones" que llama al metodo obtener_postulaciones
        self.router.get("/postulaciones")(self.obtener_postulaciones)

        # Registramos la ruta POST "/postulaciones" que llama al metodo creater_postulaciones
        self.router.post("/postulaciones")(self.creater_postulaciones)

        # Registramos la ruta PUT "/postulaciones/{id}" para actualizar una postulación existente
        self.router.put("/postulaciones/{id}")(self.actualizar_postulacion)

        # Registramos la ruta DELETE "/postulaciones/{id}" para eliminar una postulación por ID
        self.router.delete("/postulaciones/{id}")(self.eliminar_postulacion)

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
            "mensaje": "Postulación agregada con éxito",
            "postulacion": postulaciones
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/postulaciones/{id}"
    def actualizar_postulacion(self, id: int, datos: Postulaciones):
        """
        Este endpoint permite actualizar los datos de una postulación existente.
        - Parámetro `id`: ID de la postulación que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos de la postulación.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, postulacion in enumerate(self.postulaciones):
            if postulacion.Id == id:
                self.postulaciones[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Postulación no encontrada")

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/postulaciones/{id}"
    def eliminar_postulacion(self, id: int):
        """
        Este endpoint permite eliminar una postulación por su ID.
        - Parámetro `id`: ID de la postulación que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, postulacion in enumerate(self.postulaciones):
            if postulacion.Id == id:
                del self.postulaciones[i]
                return {"mensaje": "Postulación eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Postulación no encontrada")
