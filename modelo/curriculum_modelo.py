# Importamos BaseModel desde Pydantic para definir un modelo de datos con validación automática
from pydantic import BaseModel

# Definimos la clase Curriculum que hereda de BaseModel
class Curriculum(BaseModel):
    Id: int  # Identificador único del curriculum
    CandidatoId: int  # ID del candidato al que pertenece este curriculum
    Profesion: str  # Profesión principal del candidato
    Experiencias: str  # Experiencia laboral previa (puede incluir cargos, empresas, duración)
    CompetenciasLaborales: str  # Habilidades y competencias relacionadas con el trabajo
    Formacion_Complementaria: str  # Cursos, certificaciones u otra formación adicional
    Idiomas: str  # Idiomas que domina el candidato (por ejemplo: "Español nativo, Inglés intermedio")
