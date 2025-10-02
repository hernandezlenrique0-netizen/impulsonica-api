"""
Clase AdministradorAPI que define rutas para gestionar administradores en IMPULSONICA usando FastAPI.
Permite listar, agregar, actualizar y eliminar administradores con métodos HTTP (GET, POST, PUT, DELETE).
Utiliza una lista en memoria para almacenar los administradores y un APIRouter para exponer las rutas.
"""
from fastapi import APIRouter, HTTPException
from modelo.administrador_modelo import Administrador

class AdministradorAPI:
    def __init__(self):
        self.router = APIRouter()
        self.administrador = [
            Administrador(
                Id=2,
                Usuario="mariolopez2025",
                Contrasenia="MarioSecurePass!",
                Nombres="Mario",
                Apellidos="López",
                Telefono="87451236",
                MunicipioId=4,
                DepartamentoId=2
            )
        ]

        self.router.get("/administrador")(self.obtener_administrador)
        self.router.post("/administrador")(self.creater_administrador)
        self.router.put("/administrador/{id}")(self.actualizar_administrador)
        self.router.delete("/administrador/{id}")(self.eliminar_administrador)

    def obtener_administrador(self):
        print(" Se llamó a /administrador")
        return self.administrador

    def creater_administrador(self, administrador: Administrador):
        self.administrador.append(administrador)
        return {
            "mensaje": "Administrador agregado con éxito",
            "administrador": administrador
        }

    def actualizar_administrador(self, id: int, datos: Administrador):
        for i, admin in enumerate(self.administrador):
            if admin.Id == id:
                self.administrador[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Administrador no encontrado")

    def eliminar_administrador(self, id: int):
        for i, admin in enumerate(self.administrador):
            if admin.Id == id:
                del self.administrador[i]
                return {"mensaje": "Administrador eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
