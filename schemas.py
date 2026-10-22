from pydantic import BaseModel


class HouseFeatures(BaseModel):
    SqFtTotLiving: float
    SqFtLot: float
    Bedrooms: int
    Bathrooms: float
    BldgGrade: int
    YrBuilt: int
    NewConstruction: int
    TrafficNoise: float

class PredictionResponse(BaseModel):
    predicted_price_usd: float
