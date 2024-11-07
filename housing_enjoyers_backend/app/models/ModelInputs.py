from pydantic import BaseModel

# Incomplete, needs decision on what user inputs are
class ModelInputs(BaseModel):
    maxHousePrice: int


class PricePredictionRequest(BaseModel):
    price_input: int