# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Departamentos desde el archivo correspondiente
from modelo.departamentos_modelo import Departamentos

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Departamentos"
class DepartamentosAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un departamento de ejemplo (simula una base de datos en memoria)
        self.departamentos = [
            Departamentos(
                Id=1,
                Nombre="Managua"
            )
        ]

        # Registramos la ruta GET "/departamento" que llama al metodo obtener_departamentos
        self.router.get("/departamento")(self.obtener_departamentos)

        # Registramos la ruta POST "/departamento" que llama al metodo creater_departamentos
        self.router.post("/departamento")(self.creater_departamentos)

        # Registramos la ruta PUT "/departamento/{id}" para actualizar un departamento existente
        self.router.put("/departamento/{id}")(self.actualizar_departamento)

        # Registramos la ruta DELETE "/departamento/{id}" para eliminar un departamento por ID
        self.router.delete("/departamento/{id}")(self.eliminar_departamento)

    # Metodo que se ejecuta cuando se hace una petición GET a "/departamento"
    def obtener_departamentos(self):
        # Devuelve la lista de departamentos almacenados
        return self.departamentos

    # Metodo que se ejecuta cuando se hace una petición POST a "/departamento"
    def creater_departamentos(self, departamentos: Departamentos):
        # Agrega el nuevo departamento a la lista
        self.departamentos.append(departamentos)

        # Devuelve un mensaje de confirmación junto con el departamento agregado
        return {
            "mensaje": "Departamento agregado con éxito",
            "departamento": departamentos
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/departamento/{id}"
    def actualizar_departamento(self, id: int, datos: Departamentos):
        """
        Este endpoint permite actualizar los datos de un departamento existente.
        - Parámetro `id`: ID del departamento que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del departamento.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, depto in enumerate(self.departamentos):
            if depto.Id == id:
                self.departamentos[i] = datos  # Reemplaza el departamento existente con los nuevos datos
                return datos  # Devuelve el departamento actualizado
        raise HTTPException(status_code=404, detail="Departamento no encontrado")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/departamento/{id}"
    def eliminar_departamento(self, id: int):
        """
        Este endpoint permite eliminar un departamento por su ID.
        - Parámetro `id`: ID del departamento que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, depto in enumerate(self.departamentos):
            if depto.Id == id:
                del self.departamentos[i]  # Elimina el departamento de la lista
                return {"mensaje": "Departamento eliminado exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Departamento no encontrado")  # Error si no se encuentra
