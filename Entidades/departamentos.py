"""
Este módulo define la clase DepartamentosAPI, encargada de gestionar el recurso 'Departamento' en IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, crear, actualizar y eliminar departamentos.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas o prototipos iniciales.

Endpoints disponibles:
- GET /departamento: Devuelve todos los departamentos registrados.
- POST /departamento: Agrega un nuevo departamento.
- PUT /departamento/{id}: Actualiza un departamento existente por su ID.
- DELETE /departamento/{id}: Elimina un departamento por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.departamentos_modelo import Departamentos

class DepartamentosAPI:
    def __init__(self):
        self.router = APIRouter()
        self.departamentos = [
            Departamentos(
                Id=1,
                Nombre="Managua"
            )
        ]

        self.router.get("/departamento")(self.obtener_departamentos)
        self.router.post("/departamento")(self.creater_departamentos)
        self.router.put("/departamento/{id}")(self.actualizar_departamento)
        self.router.delete("/departamento/{id}")(self.eliminar_departamento)

    def obtener_departamentos(self):
        return self.departamentos

    def creater_departamentos(self, departamentos: Departamentos):
        self.departamentos.append(departamentos)
        return {
            "mensaje": "Departamento agregado con éxito",
            "departamento": departamentos
        }

    def actualizar_departamento(self, id: int, datos: Departamentos):
        for i, depto in enumerate(self.departamentos):
            if depto.Id == id:
                self.departamentos[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Departamento no encontrado")

    def eliminar_departamento(self, id: int):
        for i, depto in enumerate(self.departamentos):
            if depto.Id == id:
                del self.departamentos[i]
                return {"mensaje": "Departamento eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Departamento no encontrado")

