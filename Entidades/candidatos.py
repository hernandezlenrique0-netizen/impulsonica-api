# Importamos APIRouter desde FastAPI para crear rutas específicas
from fastapi import APIRouter

# Importamos el modelo de datos Candidatos desde otro archivo
from modelo.candidatos_modelo import Candidatos

# Definimos una clase que encapsula las rutas relacionadas con "Candidatos"
class CandidatosAPI:
    def __init__(self):
        # Creamos un router exclusivo para esta clase
        self.router = APIRouter()

        # Creamos una lista con un candidato de ejemplo (simula una base de datos en memoria)
        self.candidato = [
            Candidatos(
                Id=1,
                Usuario="juanperez2025",
                Contraseña="JuanSecurePass!",
                Nombres="Juan",
                Apellidos="Pérez",
                Genero="M",
                Email="juan.perez@example.com",
                Telefono1="87561234",
                Telefono2="88874567",
                MunicipioId=3,
                DepartamentoId=1
            )
        ]

        # Registramos la ruta GET "/candidatos" que llama al metodo obtener_candidatos
        self.router.get("/candidatos")(self.obtener_candidatos)

        # Registramos la ruta POST "/candidatos" que llama al metodo creater_candidatos
        self.router.post("/candidatos")(self.creater_candidatos)

    # Metodo que se ejecuta cuando se hace una petición GET a "/candidatos"
    def obtener_candidatos(self):
        # Devuelve la lista de candidatos almacenados
        return self.candidato

    # Metodo que se ejecuta cuando se hace una petición POST a "/candidatos"
    def creater_candidatos(self, candidato: Candidatos):
        # Agrega el nuevo candidato a la lista
        self.candidato.append(candidato)

        # Devuelve un mensaje de confirmación junto con el candidato agregado
        return {
            "mensaje ": "candidato agregado con exito",
            "candidato": candidato
        }
