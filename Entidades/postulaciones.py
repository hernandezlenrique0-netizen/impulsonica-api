"""
Este módulo define la clase PostulacionesAPI, encargada de gestionar el recurso 'Postulaciones' en el sistema IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar postulaciones laborales.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas, desarrollo local o prototipos.

Endpoints disponibles:
- GET /postulaciones: Lista todas las postulaciones registradas.
- POST /postulaciones: Agrega una nueva postulación.
- PUT /postulaciones/{id}: Actualiza los datos de una postulación existente por su ID.
- DELETE /postulaciones/{id}: Elimina una postulación por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.postulaciones_modelo import Postulaciones
from datetime import date

class PostulacionesAPI:
    def __init__(self):
        self.router = APIRouter()
        self.postulaciones = [
            Postulaciones(
                Id=1,
                CandidatoId=1,
                EmpleoId=1,
                FechaPublicación=date(2025, 9, 25),
                EstadoPostulación=True
            )
        ]

        self.router.get("/postulaciones")(self.obtener_postulaciones)
        self.router.post("/postulaciones")(self.creater_postulaciones)
        self.router.put("/postulaciones/{id}")(self.actualizar_postulacion)
        self.router.delete("/postulaciones/{id}")(self.eliminar_postulacion)

    def obtener_postulaciones(self):
        return self.postulaciones

    def creater_postulaciones(self, postulaciones: Postulaciones):
        self.postulaciones.append(postulaciones)
        return {
            "mensaje": "Postulación agregada con éxito",
            "postulacion": postulaciones
        }

    def actualizar_postulacion(self, id: int, datos: Postulaciones):
        for i, postulacion in enumerate(self.postulaciones):
            if postulacion.Id == id:
                self.postulaciones[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Postulación no encontrada")

    def eliminar_postulacion(self, id: int):
        for i, postulacion in enumerate(self.postulaciones):
            if postulacion.Id == id:
                del self.postulaciones[i]
                return {"mensaje": "Postulación eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Postulación no encontrada")

