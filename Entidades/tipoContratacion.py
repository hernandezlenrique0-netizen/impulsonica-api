# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

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

        # Registramos la ruta PUT "/Tcontratación/{id}" para actualizar un tipo de contratación existente
        self.router.put("/Tcontratación/{id}")(self.actualizar_Tcontratacion)

        # Registramos la ruta DELETE "/Tcontratación/{id}" para eliminar un tipo de contratación por ID
        self.router.delete("/Tcontratación/{id}")(self.eliminar_Tcontratacion)

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
            "mensaje": "Tipo de contratación agregada con éxito",
            "tipoContratacion": tcontratacion
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/Tcontratación/{id}"
    def actualizar_Tcontratacion(self, id: int, datos: TipoContratacion):
        """
        Este endpoint permite actualizar los datos de un tipo de contratación existente.
        - Parámetro `id`: ID del tipo de contratación que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del tipo de contratación.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, tipo in enumerate(self.tipoContratacion):
            if tipo.Id == id:
                self.tipoContratacion[i] = datos  # Reemplaza el tipo existente con los nuevos datos
                return datos  # Devuelve el tipo actualizado
        raise HTTPException(status_code=404, detail="Tipo de contratación no encontrado")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/Tcontratación/{id}"
    def eliminar_Tcontratacion(self, id: int):
        """
        Este endpoint permite eliminar un tipo de contratación por su ID.
        - Parámetro `id`: ID del tipo de contratación que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, tipo in enumerate(self.tipoContratacion):
            if tipo.Id == id:
                del self.tipoContratacion[i]  # Elimina el tipo de la lista
                return {"mensaje": "Tipo de contratación eliminada exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Tipo de contratación no encontrado")  # Error si no se encuentra
