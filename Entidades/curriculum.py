# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Curriculum desde el archivo correspondiente
from modelo.curriculum_modelo import Curriculum

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Curriculum"
class CurriculmAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un curriculum de ejemplo (simula una base de datos en memoria)
        self.curriculum = [
            Curriculum(
                Id=1,
                CandidatoId=1,
                Profesion="Ingeniería en Sistemas",
                Experiencias="1 Año como desarrollador backend en una empresa de tecnología financiera",
                CompetenciasLaborales="Dominio de bases de datos SQL, programación en Python y JavaScript, trabajo en equipo, resolución de problemas",
                Formacion_Complementaria="Curso de desarrollo web con React, certificación en ciberseguridad básica",
                Idiomas="Español nativo, Inglés intermedio"
            )
        ]

        # Registramos la ruta GET "/curriculum" que llama al metodo obtener_curriculum
        self.router.get("/curriculum")(self.obtener_curriculum)

        # Registramos la ruta POST "/curriculum" que llama al metodo creater_curriculum
        self.router.post("/curriculum")(self.creater_curriculum)

        # Registramos la ruta PUT "/curriculum/{id}" para actualizar un curriculum existente
        self.router.put("/curriculum/{id}")(self.actualizar_curriculum)

        # Registramos la ruta DELETE "/curriculum/{id}" para eliminar un curriculum por ID
        self.router.delete("/curriculum/{id}")(self.eliminar_curriculum)

    # Metodo que se ejecuta cuando se hace una petición GET a "/curriculum"
    def obtener_curriculum(self):
        # Devuelve la lista de curriculums almacenados
        return self.curriculum

    # Metodo que se ejecuta cuando se hace una petición POST a "/curriculum"
    def creater_curriculum(self, curriculum: Curriculum):
        # Agrega el nuevo curriculum a la lista
        self.curriculum.append(curriculum)

        # Devuelve un mensaje de confirmación junto con el curriculum agregado
        return {
            "mensaje": "Curriculum agregado con éxito",
            "curriculum": curriculum
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/curriculum/{id}"
    def actualizar_curriculum(self, id: int, datos: Curriculum):
        """
        Este endpoint permite actualizar los datos de un curriculum existente.
        - Parámetro `id`: ID del curriculum que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del curriculum.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, curr in enumerate(self.curriculum):
            if curr.Id == id:
                self.curriculum[i] = datos  # Reemplaza el curriculum existente con los nuevos datos
                return datos  # Devuelve el curriculum actualizado
        raise HTTPException(status_code=404, detail="Curriculum no encontrado")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/curriculum/{id}"
    def eliminar_curriculum(self, id: int):
        """
        Este endpoint permite eliminar un curriculum por su ID.
        - Parámetro `id`: ID del curriculum que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, curr in enumerate(self.curriculum):
            if curr.Id == id:
                del self.curriculum[i]  # Elimina el curriculum de la lista
                return {"mensaje": "Curriculum eliminado exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Curriculum no encontrado")  # Error si no se encuentra
