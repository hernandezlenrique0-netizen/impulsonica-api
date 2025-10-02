"""
Este módulo define la clase VacantesAPI, encargada de gestionar el recurso 'Vacantes' en el sistema IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar vacantes laborales.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas, desarrollo local o prototipos.

Endpoints disponibles:
- GET /vacantes: Lista todas las vacantes registradas.
- POST /vacantes: Agrega una nueva vacante.
- PUT /vacantes/{id}: Actualiza los datos de una vacante existente por su ID.
- DELETE /vacantes/{id}: Elimina una vacante por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.vacantes_modelo import Vacantes

class VacantesAPI:
    def __init__(self):
        self.router = APIRouter()
        self.vacante = [
            Vacantes(
                Id=1,
                Nombre="Se solicita un programador",
                CargoSolicitado="Programador web",
                NombreEmpresa="BancoLafise",
                AreaEmpresa="BancoLafise",
                TipoContratacionId=1,
                NivelExperiencia="1 Años",
                DepartementoId=1,
                MunicipioId=1,
                Email="lafise@gmail.com",
                Telefono="87654909",
                Expira="1 mes",
                Descripcion="Se busca un programador web para que crear una pagina web a la empresa",
                Requisitos="Su curriculum completo",
                EmpleosId=1
            )
        ]

        self.router.get("/vacantes")(self.obtener_vacantes)
        self.router.post("/vacantes")(self.creater_vacantes)
        self.router.put("/vacantes/{id}")(self.actualizar_vacante)
        self.router.delete("/vacantes/{id}")(self.eliminar_vacante)

    def obtener_vacantes(self):
        return self.vacante

    def creater_vacantes(self, vacante: Vacantes):
        self.vacante.append(vacante)
        return {
            "mensaje": "Vacante agregada con éxito",
            "vacante": vacante
        }

    def actualizar_vacante(self, id: int, datos: Vacantes):
        for i, vacante in enumerate(self.vacante):
            if vacante.Id == id:
                self.vacante[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Vacante no encontrada")

    def eliminar_vacante(self, id: int):
        for i, vacante in enumerate(self.vacante):
            if vacante.Id == id:
                del self.vacante[i]
                return {"mensaje": "Vacante eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Vacante no encontrada")