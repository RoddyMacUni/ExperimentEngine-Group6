from dataclasses import dataclass

@dataclass
class GenericResponse:
    code: str
    message: str