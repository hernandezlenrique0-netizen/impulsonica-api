# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Municipios desde el archivo correspondiente
from modelo.municipios_modelo import Municipios

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Municipios"
class MunicipiosAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un municipio de ejemplo (simula una base de datos en memoria)
        self.municipios = [
            Municipios(
                Id=1,
                Nombre="Tipitapa",       # Nombre del municipio
                DepartamentoId=2         # ID del departamento al que pertenece
            )
        ]

        # Registramos la ruta GET "/municipios" que llama al metodo obtener_municipios
        self.router.get("/municipios")(self.obtener_municipios)

        # Registramos la ruta POST "/municipios" que llama al metodo creater_nunicipios
        self.router.post("/municipios")(self.creater_nunicipios)

    # Metodo que se ejecuta cuando se hace una petición GET a "/municipios"
    def obtener_municipios(self):
        # Devuelve la lista de municipios almacenados
        return self.municipios

    # Metodo que se ejecuta cuando se hace una petición POST a "/municipios"
    def creater_nunicipios(self, municipio: Municipios):
        # Agrega el nuevo municipio a la lista
        self.municipios.append(municipio)

        # Devuelve un mensaje de confirmación junto con el municipio agregado
        return {
            "mensaje ": " municipio agregada con exito",
            "municipio": municipio
        }
