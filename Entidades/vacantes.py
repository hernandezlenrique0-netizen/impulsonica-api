# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

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

        # Registramos la ruta PUT "/vacantes/{id}" para actualizar una vacante existente
        self.router.put("/vacantes/{id}")(self.actualizar_vacante)

        # Registramos la ruta DELETE "/vacantes/{id}" para eliminar una vacante por ID
        self.router.delete("/vacantes/{id}")(self.eliminar_vacante)

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
            "mensaje": "Vacante agregada con éxito",
            "vacante": vacante
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/vacantes/{id}"
    def actualizar_vacante(self, id: int, datos: Vacantes):
        """
        Este endpoint permite actualizar los datos de una vacante existente.
        - Parámetro `id`: ID de la vacante que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos de la vacante.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, vacante in enumerate(self.vacante):
            if vacante.Id == id:
                self.vacante[i] = datos  # Reemplaza la vacante existente con los nuevos datos
                return datos  # Devuelve la vacante actualizada
        raise HTTPException(status_code=404, detail="Vacante no encontrada")  # Error si no se encuentra

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/vacantes/{id}"
    def eliminar_vacante(self, id: int):
        """
        Este endpoint permite eliminar una vacante por su ID.
        - Parámetro `id`: ID de la vacante que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, vacante in enumerate(self.vacante):
            if vacante.Id == id:
                del self.vacante[i]  # Elimina la vacante de la lista
                return {"mensaje": "Vacante eliminada exitosamente"}  # Mensaje de éxito
        raise HTTPException(status_code=404, detail="Vacante no encontrada")  # Error si no se encuentra



