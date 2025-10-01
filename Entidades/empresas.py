# Importamos APIRouter desde FastAPI para definir rutas específicas
from fastapi import APIRouter, HTTPException

# Importamos el modelo de datos Empresas desde el archivo correspondiente
from modelo.empresas_modelo import Empresas

# Definimos una clase que encapsula las rutas relacionadas con el recurso "Empresas"
class EmpresasAPI:
    def __init__(self):
        self.router = APIRouter()
        self.empresas = [
            Empresas(
                Id=1,
                Nombres="Banco Lafise",  # Nombre de la empresa
                Usuario="lafise_admin",  # Usuario de acceso para la empresa
                Contraseña="LafiseSecure2025!",  # Contraseña de acceso
                Descripcion="Empresa financiera con presencia nacional",  # Breve descripción de la empresa
                Actividad="Servicios bancarios",  # Actividad principal de la empresa
                Email="contacto@lafise.com",  # Correo electrónico de contacto
                Telefono="82547890",  # Teléfono de contacto
                MunicipioId=5,  # ID del municipio donde se ubica la empresa
                DepartamentoId=2  # ID del departamento correspondiente
            )
        ]

        # Registramos la ruta GET "/empresas" que llama al metodo obtener_empresas
        self.router.get("/empresas")(self.obtener_empresas)

        # Registramos la ruta POST "/empresas" que llama al metodo creater_empresas
        self.router.post("/empresas")(self.creater_empresas)

        # Registramos la ruta PUT "/empresas/{id}" para actualizar una empresa existente
        self.router.put("/empresas/{id}")(self.actualizar_empresa)

        # Registramos la ruta DELETE "/empresas/{id}" para eliminar una empresa por ID
        self.router.delete("/empresas/{id}")(self.eliminar_empresa)

    # Metodo que se ejecuta cuando se hace una petición GET a "/empresas"
    def obtener_empresas(self):
        # Devuelve la lista de empresas almacenadas
        return self.empresas

    # Metodo que se ejecuta cuando se hace una petición POST a "/empresas"
    def creater_empresas(self, empresas: Empresas):
        # Agrega la nueva empresa a la lista
        self.empresas.append(empresas)

        # Devuelve un mensaje de confirmación junto con la empresa agregada
        return {
            "mensaje": "Empresa agregada con éxito",
            "empresas": empresas
        }

    # Metodo que se ejecuta cuando se hace una petición PUT a "/empresas/{id}"
    def actualizar_empresa(self, id: int, datos: Empresas):
        """
        Este endpoint permite actualizar los datos de una empresa existente.
        - Parámetro `id`: ID de la empresa que se desea actualizar.
        - Parámetro `datos`: Objeto con los nuevos datos de la empresa.
        - Retorna: El objeto actualizado si se encuentra, o un error 404 si no existe.
        """
        for i, empresa in enumerate(self.empresas):
            if empresa.Id == id:
                self.empresas[i] = datos
                return datos
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    # Metodo que se ejecuta cuando se hace una petición DELETE a "/empresas/{id}"
    def eliminar_empresa(self, id: int):
        """
        Este endpoint permite eliminar una empresa por su ID.
        - Parámetro `id`: ID de la empresa que se desea eliminar.
        - Retorna: Un mensaje de confirmación si se elimina, o un error 404 si no existe.
        """
        for i, empresa in enumerate(self.empresas):
            if empresa.Id == id:
                del self.empresas[i]
                return {"mensaje": "Empresa eliminada exitosamente"}
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
