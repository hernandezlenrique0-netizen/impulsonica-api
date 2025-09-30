# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

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
            "mensaje ": "curriculum agregado con exito",
            "curriculum": curriculum
        }
