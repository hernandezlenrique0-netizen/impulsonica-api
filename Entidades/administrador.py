# Importamos APIRouter desde FastAPI para crear rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Administrador desde otro archivo
from modelo.administrador_modelo import Administrador

# Definimos una clase que encapsula las rutas relacionadas con "Administrador"
class AdministradorAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un administrador de ejemplo (simula una base de datos en memoria)
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

        # Registramos la ruta GET "/administrador" que llama al metodo obtener_administrador
        self.router.get("/administrador")(self.obtener_administrador)

        # Registramos la ruta POST "/administrador" que llama al metodo creater_administrador
        self.router.post("/administrador")(self.creater_administrador)

        # Registramos la ruta PUT "/administrador/{id}" para actualizar un administrador existente
        self.router.put("/administrador/{id}")(self.actualizar_administrador)

        # Registramos la ruta DELETE "/administrador/{id}" para eliminar un administrador por ID
        self.router.delete("/administrador/{id}")(self.eliminar_administrador)

    # Metodo que se ejecuta cuando se hace una petición GET a "/administrador"
    def obtener_administrador(self):
        print(" Se llamó a /administrador")  # Mensaje de depuración en consola
        return self.administrador  # Devuelve la lista de administradores

    # Metodo que se ejecuta cuando se hace una petición POST a "/administrador"
    def creater_administrador(self, administrador: Administrador):
        self.administrador.append(administrador)  # Agrega el nuevo administrador a la lista
        return {
            "mensaje": "Administrador agregado con éxito",  # Mensaje de confirmación
            "administrador": administrador  # Devuelve el administrador recién agregado
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/administrador/{id}"
    def actualizar_administrador(self, id: int, datos: Administrador):
        """
        Este endpoint permite actualizar los datos de un administrador existente.
        - Parámetro `id`: ID del administrador que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del administrador.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, admin in enumerate(self.administrador):
            if admin.Id == id:
                self.administrador[i] = datos  # Reemplaza el administrador existente con los nuevos datos
                return datos  # Devuelve el administrador actualizado
        raise HTTPException(status_code=404, detail="Administrador no encontrado")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/administrador/{id}"
    def eliminar_administrador(self, id: int):
        """
        Este endpoint permite eliminar un administrador por su ID.
        - Parámetro `id`: ID del administrador que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, admin in enumerate(self.administrador):
            if admin.Id == id:
                del self.administrador[i]  # Elimina el administrador de la lista
                return {"mensaje": "Administrador eliminado exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Administrador no encontrado")  # Error si no se encuentra
