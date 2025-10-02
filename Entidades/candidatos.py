"""
Clase CandidatosAPI que define rutas para gestionar candidatos en IMPULSONICA usando FastAPI.
Permite listar, agregar, actualizar y eliminar candidatos mediante métodos HTTP (GET, POST, PUT, DELETE).
Utiliza una lista en memoria como almacenamiento temporal y expone las rutas a través de APIRouter.
"""
from fastapi import APIRouter, HTTPException
from modelo.candidatos_modelo import Candidatos

class CandidatosAPI:
    def __init__(self):
        self.router = APIRouter()
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

        self.router.get("/candidatos")(self.obtener_candidatos)
        self.router.post("/candidatos")(self.creater_candidatos)
        self.router.put("/candidatos/{id}")(self.actualizar_candidato)
        self.router.delete("/candidatos/{id}")(self.eliminar_candidato)

    def obtener_candidatos(self):
        return self.candidato

    def creater_candidatos(self, candidato: Candidatos):
        self.candidato.append(candidato)
        return {
            "mensaje": "Candidato agregado con éxito",
            "candidato": candidato
        }

    def actualizar_candidato(self, id: int, datos: Candidatos):
        for i, candidato in enumerate(self.candidato):
            if candidato.Id == id:
                self.candidato[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    def eliminar_candidato(self, id: int):
        for i, candidato in enumerate(self.candidato):
            if candidato.Id == id:
                del self.candidato[i]
                return {"mensaje": "Candidato eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

