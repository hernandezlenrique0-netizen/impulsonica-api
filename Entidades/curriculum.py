"""
Clase CurriculmAPI que gestiona rutas relacionadas al recurso Curriculum en IMPULSONICA usando FastAPI.
Permite listar, agregar, actualizar y eliminar curriculums mediante métodos HTTP (GET, POST, PUT, DELETE).
Utiliza una lista en memoria como almacenamiento temporal y expone las rutas con APIRouter.
"""
from fastapi import APIRouter, HTTPException
from modelo.curriculum_modelo import Curriculum

class CurriculmAPI:
    def __init__(self):
        self.router = APIRouter()
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

        self.router.get("/curriculum")(self.obtener_curriculum)
        self.router.post("/curriculum")(self.creater_curriculum)
        self.router.put("/curriculum/{id}")(self.actualizar_curriculum)
        self.router.delete("/curriculum/{id}")(self.eliminar_curriculum)

    def obtener_curriculum(self):
        return self.curriculum

    def creater_curriculum(self, curriculum: Curriculum):
        self.curriculum.append(curriculum)
        return {
            "mensaje": "Curriculum agregado con éxito",
            "curriculum": curriculum
        }

    def actualizar_curriculum(self, id: int, datos: Curriculum):
        for i, curr in enumerate(self.curriculum):
            if curr.Id == id:
                self.curriculum[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Curriculum no encontrado")

    def eliminar_curriculum(self, id: int):
        for i, curr in enumerate(self.curriculum):
            if curr.Id == id:
                del self.curriculum[i]
                return {"mensaje": "Curriculum eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Curriculum no encontrado")

