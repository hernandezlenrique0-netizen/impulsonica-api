# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Municipios desde el archivo correspondiente
from modelo.municipios_modelo import Municipios

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Municipios"
class MunicipiosAPI:
    def __init__(self):
        self.router = APIRouter()
        self.municipios = [
            Municipios(
                Id=1,
                Nombre="Tipitapa",       # Nombre del municipio
                DepartamentoId=2         # ID del departamento al que pertenece
            )
        ]

        # Registramos la ruta GET "/municipios" que llama al metodo obtener_municipios
        self.router.get("/municipios")(self.obtener_municipios)

        # Registramos la ruta POST "/municipios" que llama al metodo creater_nunicipios
        self.router.post("/municipios")(self.creater_nunicipios)

        # Registramos la ruta PUT "/municipios/{id}" para actualizar un municipio existente
        self.router.put("/municipios/{id}")(self.actualizar_municipio)

        # Registramos la ruta DELETE "/municipios/{id}" para eliminar un municipio por ID
        self.router.delete("/municipios/{id}")(self.eliminar_municipio)

    # Metodo que se ejecuta cuando se hace una petición GET a "/municipios"
    def obtener_municipios(self):
        # Devuelve la lista de municipios almacenados
        return self.municipios

    # Metodo que se ejecuta cuando se hace una petición POST a "/municipios"
    def creater_nunicipios(self, municipio: Municipios):
        # Agrega el nuevo municipio a la lista
        self.municipios.append(municipio)

        # Devuelve un mensaje de confirmación junto con el municipio agregado
        return {
            "mensaje": "Municipio agregado con éxito",
            "municipio": municipio
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/municipios/{id}"
    def actualizar_municipio(self, id: int, datos: Municipios):
        """
        Este endpoint permite actualizar los datos de un municipio existente.
        - Parámetro `id`: ID del municipio que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del municipio.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, municipio in enumerate(self.municipios):
            if municipio.Id == id:
                self.municipios[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Municipio no encontrado")

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/municipios/{id}"
    def eliminar_municipio(self, id: int):
        """
        Este endpoint permite eliminar un municipio por su ID.
        - Parámetro `id`: ID del municipio que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, municipio in enumerate(self.municipios):
            if municipio.Id == id:
                del self.municipios[i]
                return {"mensaje": "Municipio eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
