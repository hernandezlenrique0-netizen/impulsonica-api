#  IMPULSONICA API

IMPULSONICA es una API desarrollada con FastAPI que gestiona información relacionada con 
empleos, empresas, postulaciones, vacantes y más. Está diseñada para facilitar la 
busqueda de ofertas laborales y postulaciones en Nicaragua en beneficio a empresas y candidatos.
##  Tecnologías utilizadas

- **Python 3.13+**
- **FastAPI** – Framework principal para construir la API
- **Pydantic** – Validación de datos
- **Uvicorn** – Servidor ASGI para desarrollo
- **Postman / Swagger UI** – Para pruebas y documentación

##  Estructura del proyecto

MPULSONICA/ 
- ├── Entidades/ # Rutas y lógica de cada entidad 
- ├── modelo/ # Modelos Pydantic para validación 
- ├── static/ # Archivos estáticos (favicon, etc.) 
- ├── main.py # Archivo principal de la API


## Endpoints disponibles

### Vacantes

- `GET /vacantes` – Lista todas las vacantes disponibles  
- `POST /vacantes` – Crea una nueva vacante  
- `PUT /vacantes/{id}` – Actualiza una vacante por ID  
- `DELETE /vacantes/{id}` – Elimina una vacante por ID  

### Postulaciones

- `GET /postulaciones` – Lista todas las postulaciones  
- `POST /postulaciones` – Permite a un candidato postularse  
- `PUT /postulaciones/{id}` – Actualiza una postulación por ID  
- `DELETE /postulaciones/{id}` – Elimina una postulación por ID  

### Empresas

- `GET /empresas` – Consulta empresas registradas  
- `POST /empresas` – Registra una nueva empresa  
- `PUT /empresas/{id}` – Actualiza una empresa por ID  
- `DELETE /empresas/{id}` – Elimina una empresa por ID  

### Tipo de Contratación

- `GET /Tcontratación` – Tipos de contratación disponibles  
- `POST /Tcontratación` – Crea un nuevo tipo de contratación  
- `PUT /Tcontratación/{id}` – Actualiza un tipo de contratación por ID  
- `DELETE /Tcontratación/{id}` – Elimina un tipo de contratación por ID  

### Empleos

- `GET /empleos` – Lista todas las ofertas de empleo  
- `POST /empleos` – Crea una nueva oferta de empleo  
- `PUT /empleos/{id}` – Actualiza una oferta de empleo por ID  
- `DELETE /empleos/{id}` – Elimina una oferta de empleo por ID  

### Departamentos

- `GET /departamento` – Lista todos los departamentos  
- `POST /departamento` – Crea un nuevo departamento  
- `PUT /departamento/{id}` – Actualiza un departamento por ID  
- `DELETE /departamento/{id}` – Elimina un departamento por ID  

### Municipios

- `GET /municipios` – Lista todos los municipios  
- `POST /municipios` – Crea un nuevo municipio  
- `PUT /municipios/{id}` – Actualiza un municipio por ID  
- `DELETE /municipios/{id}` – Elimina un municipio por ID  

### Candidatos

- `GET /candidatos` – Lista todos los candidatos registrados  
- `POST /candidatos` – Registra un nuevo candidato  
- `PUT /candidatos/{id}` – Actualiza un candidato por ID  
- `DELETE /candidatos/{id}` – Elimina un candidato por ID  

### Curriculum

- `GET /curriculum` – Lista todos los currículums registrados  
- `POST /curriculum` – Crea un nuevo currículum  
- `PUT /curriculum/{id}` – Actualiza un currículum por ID  
- `DELETE /curriculum/{id}` – Elimina un currículum por ID  

### Administrador

- `GET /administrador` – Lista todos los administradores  
- `POST /administrador` – Registra un nuevo administrador  
- `PUT /administrador/{id}` – Actualiza un administrador por ID  
- `DELETE /administrador/{id}` – Elimina un administrador por ID  


Consulta toda la documentación en:

- [http://localhost:8000/docs](http://localhost:8000/docs) – Swagger UI
- [http://localhost:8000/redoc](http://localhost:8000/redoc) – ReDoc

##  Cómo ejecutar el proyecto localmente

```bash
# Clona el repositorio
git clone https://github.com/hernandezlenrique0-netizen/impulsonica-api.git
cd impulsonica-api

# Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt
```
Desarrollado por:
- Luis Enrique Hernández Lorío
- Irma Mayerling Diaz vargas
- Danilo Antonio Larios Perez
- Dylan Antuan Lopez Lopez

- Email:
-  [hernandezlenrique0@gmail.com]
-  [dylanantuan341@gmail.com]
-  [Danilolarios59@gmail.com]
-  [virma9484@gmail.com]
- GitHub: hernandezlenrique0-netizen

# Ejecuta el servidor
uvicorn main:app --reload
