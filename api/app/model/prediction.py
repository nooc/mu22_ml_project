from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """Prediction request

    Args:
        BaseModel (_type_): _description_
    """
    news:list[str]
    stock:list[float]

class PredictionResponse(BaseModel):
    """Prediction response

    Args:
        BaseModel (_type_): _description_
    """
    value:float
    message:str
