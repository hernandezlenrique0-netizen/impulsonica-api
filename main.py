from fastapi import FastAPI

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

app = FastAPI()

app.include_router(AdministradorAPI().router)
app.include_router(CandidatosAPI().router)
app.include_router(CurriculmAPI().router)
app.include_router(DepartamentosAPI().router)
app.include_router(EmpleosAPI().router)
app.include_router(EmpresasAPI().router)
app.include_router(MunicipiosAPI().router)
app.include_router(PostulacionesAPI().router)
app.include_router(TipoContratacionAPI().router)
app.include_router(VacantesAPI().router)

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
