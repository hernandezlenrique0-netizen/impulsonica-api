# Importamos APIRouter desde FastAPI para crear rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Candidatos desde otro archivo
from modelo.candidatos_modelo import Candidatos

# Definimos una clase que encapsula las rutas relacionadas con "Candidatos"
class CandidatosAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un candidato de ejemplo (simula una base de datos en memoria)
        self.candidato = [
            Candidatos(
                Id=1,
                Usuario="juanperez2025",
                Contraseña="JuanSecurePass!",
                Nombres="Juan",
                Apellidos="Pérez",
                Genero="M",
                Email="juan.perez@example.com",
                Telefono1="87561234",
                Telefono2="88874567",
                MunicipioId=3,
                DepartamentoId=1
            )
        ]

        # Registramos la ruta GET "/candidatos" que llama al metodo obtener_candidatos
        self.router.get("/candidatos")(self.obtener_candidatos)

        # Registramos la ruta POST "/candidatos" que llama al metodo creater_candidatos
        self.router.post("/candidatos")(self.creater_candidatos)

        # Registramos la ruta PUT "/candidatos/{id}" para actualizar un candidato existente
        self.router.put("/candidatos/{id}")(self.actualizar_candidato)

        # Registramos la ruta DELETE "/candidatos/{id}" para eliminar un candidato por ID
        self.router.delete("/candidatos/{id}")(self.eliminar_candidato)

    # Metodo que se ejecuta cuando se hace una petición GET a "/candidatos"
    def obtener_candidatos(self):
        # Devuelve la lista de candidatos almacenados
        return self.candidato

    # Metodo que se ejecuta cuando se hace una petición POST a "/candidatos"
    def creater_candidatos(self, candidato: Candidatos):
        # Agrega el nuevo candidato a la lista
        self.candidato.append(candidato)

        # Devuelve un mensaje de confirmación junto con el candidato agregado
        return {
            "mensaje": "Candidato agregado con éxito",
            "candidato": candidato
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/candidatos/{id}"
    def actualizar_candidato(self, id: int, datos: Candidatos):
        """
        Este endpoint permite actualizar los datos de un candidato existente.
        - Parámetro `id`: ID del candidato que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del candidato.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, candidato in enumerate(self.candidato):
            if candidato.Id == id:
                self.candidato[i] = datos  # Reemplaza el candidato existente con los nuevos datos
                return datos  # Devuelve el candidato actualizado
        raise HTTPException(status_code=404, detail="Candidato no encontrado")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/candidatos/{id}"
    def eliminar_candidato(self, id: int):
        """
        Este endpoint permite eliminar un candidato por su ID.
        - Parámetro `id`: ID del candidato que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, candidato in enumerate(self.candidato):
            if candidato.Id == id:
                del self.candidato[i]  # Elimina el candidato de la lista
                return {"mensaje": "Candidato eliminado exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Candidato no encontrado")  # Error si no se encuentra
