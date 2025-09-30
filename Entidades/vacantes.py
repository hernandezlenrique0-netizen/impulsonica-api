# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Vacantes desde el archivo correspondiente
from modelo.vacantes_modelo import Vacantes

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Vacantes"
class VacantesAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con una vacante de ejemplo (simula una base de datos en memoria)
        self.vacante = [
            Vacantes(
                Id=1,  # ID único de la vacante
                Nombre="Se solicita un programador",  # Título general de la vacante
                CargoSolicitado="Programador web",  # Cargo específico que se está solicitando
                NombreEmpresa="BancoLafise",  # Nombre de la empresa que publica la vacante
                AreaEmpresa="BancoLafise",  # Área o sector de la empresa
                TipoContratacionId=1,  # ID del tipo de contratación (por ejemplo, tiempo completo)
                NivelExperiencia="1 Años",  # Nivel de experiencia requerido
                DepartementoId=1,  # ID del departamento donde se ubica la vacante
                MunicipioId=1,  # ID del municipio correspondiente
                Email="lafise@gmail.com",  # Correo de contacto para postulaciones
                Telefono="87654909",  # Teléfono de contacto
                Expira="1 mes",  # Tiempo de vigencia de la vacante
                Descripcion="Se busca un programador web para que crear una pagina web a la empresa",  # Descripción del trabajo
                Requisitos="Su curriculum completo",  # Requisitos que debe cumplir el postulante
                EmpleosId=1  # ID del empleo relacionado (si está vinculado a otra tabla)
            )
        ]

        # Registramos la ruta GET "/vacantes" que llama al metodo obtener_vacantes
        self.router.get("/vacantes")(self.obtener_vacantes)

        # Registramos la ruta POST "/vacantes" que llama al metodo creater_vacantes
        self.router.post("/vacantes")(self.creater_vacantes)

    # Metodo que se ejecuta cuando se hace una petición GET a "/vacantes"
    def obtener_vacantes(self):
        # Devuelve la lista de vacantes almacenadas
        return self.vacante

    # Metodo que se ejecuta cuando se hace una petición POST a "/vacantes"
    def creater_vacantes(self, vacante: Vacantes):
        # Agrega la nueva vacante a la lista
        self.vacante.append(vacante)

        # Devuelve un mensaje de confirmación junto con la vacante agregada
        return {
            "mensaje ": "vacante agregado con exito",
            "vacante": vacante
        }



