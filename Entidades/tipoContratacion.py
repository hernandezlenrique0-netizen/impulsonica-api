"""
Este módulo define la clase TipoContratacionAPI, encargada de gestionar el recurso 'Tipo de Contratación' en el sistema IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar tipos de contratación laboral.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas, desarrollo local o prototipos.

Endpoints disponibles:
- GET /Tcontratación: Lista todos los tipos de contratación registrados.
- POST /Tcontratación: Agrega un nuevo tipo de contratación.
- PUT /Tcontratación/{id}: Actualiza los datos de un tipo de contratación existente por su ID.
- DELETE /Tcontratación/{id}: Elimina un tipo de contratación por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.tipoContratacion_modelo import TipoContratacion

class TipoContratacionAPI:
    def __init__(self):
        self.router = APIRouter()
        self.tipoContratacion = [
            TipoContratacion(
                Id=1,
                Nombre="Tiempo Completo"
            )
        ]

        self.router.get("/Tcontratación")(self.obtener_Tcontrataciones)
        self.router.post("/Tcontratación")(self.creater_Tcontrataciones)
        self.router.put("/Tcontratación/{id}")(self.actualizar_Tcontratacion)
        self.router.delete("/Tcontratación/{id}")(self.eliminar_Tcontratacion)

    def obtener_Tcontrataciones(self):
        return self.tipoContratacion

    def creater_Tcontrataciones(self, tcontratacion: TipoContratacion):
        self.tipoContratacion.append(tcontratacion)
        return {
            "mensaje": "Tipo de contratación agregada con éxito",
            "tipoContratacion": tcontratacion
        }

    def actualizar_Tcontratacion(self, id: int, datos: TipoContratacion):
        for i, tipo in enumerate(self.tipoContratacion):
            if tipo.Id == id:
                self.tipoContratacion[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Tipo de contratación no encontrado")

    def eliminar_Tcontratacion(self, id: int):
        for i, tipo in enumerate(self.tipoContratacion):
            if tipo.Id == id:
                del self.tipoContratacion[i]
                return {"mensaje": "Tipo de contratación eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Tipo de contratación no encontrado")

