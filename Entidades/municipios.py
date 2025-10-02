"""
Este módulo define la clase MunicipiosAPI, encargada de gestionar el recurso 'Municipios' dentro del sistema IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar municipios.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas, desarrollo local o prototipos.

Endpoints disponibles:
- GET /municipios: Lista todos los municipios registrados.
- POST /municipios: Agrega un nuevo municipio.
- PUT /municipios/{id}: Actualiza los datos de un municipio existente por su ID.
- DELETE /municipios/{id}: Elimina un municipio por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.municipios_modelo import Municipios

class MunicipiosAPI:
    def __init__(self):
        self.router = APIRouter()
        self.municipios = [
            Municipios(
                Id=1,
                Nombre="Tipitapa",
                DepartamentoId=2
            )
        ]

        self.router.get("/municipios")(self.obtener_municipios)
        self.router.post("/municipios")(self.creater_nunicipios)
        self.router.put("/municipios/{id}")(self.actualizar_municipio)
        self.router.delete("/municipios/{id}")(self.eliminar_municipio)

    def obtener_municipios(self):
        return self.municipios

    def creater_nunicipios(self, municipio: Municipios):
        self.municipios.append(municipio)
        return {
            "mensaje": "Municipio agregado con éxito",
            "municipio": municipio
        }

    def actualizar_municipio(self, id: int, datos: Municipios):
        for i, municipio in enumerate(self.municipios):
            if municipio.Id == id:
                self.municipios[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Municipio no encontrado")

    def eliminar_municipio(self, id: int):
        for i, municipio in enumerate(self.municipios):
            if municipio.Id == id:
                del self.municipios[i]
                return {"mensaje": "Municipio eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Municipio no encontrado")

