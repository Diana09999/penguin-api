from pydantic import BaseModel, Field

class PenguinInput(BaseModel):
    bill_length_mm: float = Field(
        ...,
        gt=0,
        example=39.1,
        description="Longueur du bec (mm)"
    )

    bill_depth_mm: float = Field(
        ...,
        gt=0,
        example=18.7,
        description="Hauteur du bec (mm)"
    )

    flipper_length_mm: float = Field(
        ...,
        gt=0,
        example=181.0,
        description="Longueur de la nageoire (mm)"
    )

    body_mass_g: float = Field(
        ...,
        gt=0,
        example=3750.0,
        description="Poids (g)"
    )


class PredictionOutput(BaseModel):
    species: str
    confidence: float
    message: str


class AnalysisOutput(BaseModel):
    species: str
    confidence: float
    description: str

