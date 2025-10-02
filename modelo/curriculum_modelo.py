from pydantic import BaseModel

class Curriculum(BaseModel):
    Id: int
    CandidatoId: int
    Profesion: str
    Experiencias: str
    CompetenciasLaborales: str
    Formacion_Complementaria: str
    Idiomas: str

