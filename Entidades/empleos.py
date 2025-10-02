"""
Este módulo define la clase EmpleosAPI, encargada de gestionar las ofertas de empleo en IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar empleos.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas o prototipos iniciales.

Endpoints disponibles:
- GET /empleos: Lista todas las ofertas de empleo registradas.
- POST /empleos: Agrega una nueva oferta de empleo.
- PUT /empleos/{id}: Actualiza una oferta existente por su ID.
- DELETE /empleos/{id}: Elimina una oferta de empleo por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.empleos_modelo import Empleos
from datetime import date

class EmpleosAPI:
    def __init__(self):
        self.router = APIRouter()
        self.empleos = [
            Empleos(
                Id=2,
                Nombre="Desarrollador Web Junior",
                Descripción="Se busca desarrollador web con conocimientos en HTML, CSS y JavaScript.",
                Ubicación="Managua",
                Salario="USD 800 mensuales",
                FechaPublicación=date(year=2025, month=4, day=21),
                FechaExpiración=date(year=2025, month=9, day=25),
                EmpresaId=1,
                DepartamentoId=2
            )
        ]

        self.router.get("/empleos")(self.obtener_empleos)
        self.router.post("/empleos")(self.creater_empleos)
        self.router.put("/empleos/{id}")(self.actualizar_empleo)
        self.router.delete("/empleos/{id}")(self.eliminar_empleo)

    def obtener_empleos(self):
        return self.empleos

    def creater_empleos(self, empleos: Empleos):
        self.empleos.append(empleos)
        return {
            "mensaje": "Empleo agregado con éxito",
            "empleo": empleos
        }

    def actualizar_empleo(self, id: int, datos: Empleos):
        for i, empleo in enumerate(self.empleos):
            if empleo.Id == id:
                self.empleos[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Empleo no encontrado")

    def eliminar_empleo(self, id: int):
        for i, empleo in enumerate(self.empleos):
            if empleo.Id == id:
                del self.empleos[i]
                return {"mensaje": "Empleo eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Empleo no encontrado")
