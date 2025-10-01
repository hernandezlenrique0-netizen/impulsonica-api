# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Empleos desde el archivo correspondiente
from modelo.empleos_modelo import Empleos

# Importamos la clase date para manejar fechas
from datetime import date

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Empleos"
class EmpleosAPI:
    def __init__(self):
        self.router = APIRouter()
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

        # Registramos la ruta PUT "/empleos/{id}" para actualizar una oferta de empleo existente
        self.router.put("/empleos/{id}")(self.actualizar_empleo)

        # Registramos la ruta DELETE "/empleos/{id}" para eliminar una oferta de empleo por ID
        self.router.delete("/empleos/{id}")(self.eliminar_empleo)

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
            "mensaje": "Empleo agregado con éxito",
            "empleo": empleos
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/empleos/{id}"
    def actualizar_empleo(self, id: int, datos: Empleos):
        """
        Este endpoint permite actualizar los datos de una oferta de empleo existente.
        - Parámetro `id`: ID del empleo que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos del empleo.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, empleo in enumerate(self.empleos):
            if empleo.Id == id:
                self.empleos[i] = datos  # Reemplaza el empleo existente con los nuevos datos
                return datos
        raise HTTPException(status_code=404, detail="Empleo no encontrado")

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/empleos/{id}"
    def eliminar_empleo(self, id: int):
        """
        Este endpoint permite eliminar una oferta de empleo por su ID.
        - Parámetro `id`: ID del empleo que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, empleo in enumerate(self.empleos):
            if empleo.Id == id:
                del self.empleos[i]  # Elimina el empleo de la lista
                return {"mensaje": "Empleo eliminado exitosamente"}
        raise HTTPException(status_code=404, detail="Empleo no encontrado")
