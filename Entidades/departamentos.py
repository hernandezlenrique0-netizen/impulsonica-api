# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

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
            "mensaje ": " departamento agregada con exito",
            "departamento": departamentos
        }
