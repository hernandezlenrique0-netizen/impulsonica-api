# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Empleos desde el archivo correspondiente
from modelo.empleos_modelo import Empleos

# Importamos la clase date para manejar fechas
from datetime import date

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Empleos"
class EmpleosAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con una oferta de empleo de ejemplo (simula una base de datos en memoria)
        self.empleos = [
            Empleos(
                Id=2,
                Nombre="Desarrollador Web Junior",
                Descripción="Se busca desarrollador web con conocimientos en HTML, CSS y JavaScript.",
                Ubicación="Managua",
                Salario="USD 800 mensuales",
                FechaPublicación=date(year=2025, month=4, day=21),  # Fecha en que se publicó la oferta
                FechaExpiración=date(year=2025, month=9, day=25),   # Fecha en que expira la oferta
                EmpresaId=1,        # ID de la empresa que publica el empleo
                DepartamentoId=2    # ID del departamento donde se ubica el empleo
            )
        ]

        # Registramos la ruta GET "/empleos" que llama al metodo obtener_empleos
        self.router.get("/empleos")(self.obtener_empleos)

        # Registramos la ruta POST "/empleos" que llama al metodo creater_empleos
        self.router.post("/empleos")(self.creater_empleos)

    # Metodo que se ejecuta cuando se hace una petición GET a "/empleos"
    def obtener_empleos(self):
        # Devuelve la lista de empleos almacenados
        return self.empleos

    # Metodo que se ejecuta cuando se hace una petición POST a "/empleos"
    def creater_empleos(self, empleos: Empleos):
        # Agrega el nuevo empleo a la lista
        self.empleos.append(empleos)

        # Devuelve un mensaje de confirmación junto con el empleo agregado
        return {
            "mensaje ": " empleo agregado con exito",
            "empleo": empleos
        }
