"""
Este módulo define la clase EmpresasAPI, encargada de gestionar el recurso 'Empresas' dentro del sistema IMPULSONICA.
Utiliza FastAPI para exponer rutas HTTP que permiten consultar, registrar, actualizar y eliminar empresas.
Los datos se almacenan temporalmente en una lista en memoria, útil para pruebas, desarrollo local o prototipos.

Endpoints disponibles:
- GET /empresas: Lista todas las empresas registradas.
- POST /empresas: Agrega una nueva empresa.
- PUT /empresas/{id}: Actualiza los datos de una empresa existente por su ID.
- DELETE /empresas/{id}: Elimina una empresa por su ID.
"""
from fastapi import APIRouter, HTTPException
from modelo.empresas_modelo import Empresas

class EmpresasAPI:
    def __init__(self):
        self.router = APIRouter()
        self.empresas = [
            Empresas(
                Id=1,
                Nombres="Banco Lafise",
                Usuario="lafise_admin",
                Contraseña="LafiseSecure2025!",
                Descripcion="Empresa financiera con presencia nacional",
                Actividad="Servicios bancarios",
                Email="contacto@lafise.com",
                Telefono="82547890",
                MunicipioId=5,
                DepartamentoId=2
            )
        ]

        self.router.get("/empresas")(self.obtener_empresas)
        self.router.post("/empresas")(self.creater_empresas)
        self.router.put("/empresas/{id}")(self.actualizar_empresa)
        self.router.delete("/empresas/{id}")(self.eliminar_empresa)

    def obtener_empresas(self):
        return self.empresas

    def creater_empresas(self, empresas: Empresas):
        self.empresas.append(empresas)
        return {
            "mensaje": "Empresa agregada con éxito",
            "empresas": empresas
        }

    def actualizar_empresa(self, id: int, datos: Empresas):
        for i, empresa in enumerate(self.empresas):
            if empresa.Id == id:
                self.empresas[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    def eliminar_empresa(self, id: int):
        for i, empresa in enumerate(self.empresas):
            if empresa.Id == id:
                del self.empresas[i]
                return {"mensaje": "Empresa eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

