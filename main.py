# Importamos FastAPI para crear la aplicación principal
from fastapi import FastAPI

# Importamos las clases API desde los módulos de entidades
from Entidades.administrador import AdministradorAPI
from Entidades.candidatos import CandidatosAPI
from Entidades.curriculum import CurriculmAPI
from Entidades.departamentos import DepartamentosAPI
from Entidades.empleos import EmpleosAPI
from Entidades.empresas import EmpresasAPI
from Entidades.municipios import MunicipiosAPI
from Entidades.postulaciones import PostulacionesAPI
from Entidades.tipoContratacion import TipoContratacionAPI
from Entidades.vacantes import VacantesAPI

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Registramos cada router de las entidades en la aplicación principal
# Esto permite que cada grupo de rutas esté organizado por su clase correspondiente
app.include_router(AdministradorAPI().router)       # Rutas para administradores
app.include_router(CandidatosAPI().router)          # Rutas para candidatos
app.include_router(CurriculmAPI().router)           # Rutas para currículum
app.include_router(DepartamentosAPI().router)       # Rutas para departamentos
app.include_router(EmpleosAPI().router)             # Rutas para empleos
app.include_router(EmpresasAPI().router)            # Rutas para empresas
app.include_router(MunicipiosAPI().router)          # Rutas para municipios
app.include_router(PostulacionesAPI().router)       # Rutas para postulaciones
app.include_router(TipoContratacionAPI().router)    # Rutas para tipo de contratación
app.include_router(VacantesAPI().router)            # Rutas para vacantes

# Ruta raíz de la API, útil para verificar que el servidor está funcionando
@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido a IMPULSONICA API!"}

# Importamos StaticFiles para servir archivos estáticos como imágenes, CSS, JS, etc.
from fastapi.staticfiles import StaticFiles

# Importamos FileResponse para enviar archivos directamente como respuesta
from fastapi.responses import FileResponse

# Montamos el directorio "static" en la ruta "/static"
# Esto permite acceder a archivos estáticos desde esa ruta
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta específica para servir el ícono del sitio (favicon)
@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico")
