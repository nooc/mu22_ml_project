from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """Prediction request

    Args:
        BaseModel (_type_): _description_
    """
    daily_news:list[str]
    daily_stock:list[float]

class PredictionResponse(BaseModel):
    """Prediction response

    Args:
        BaseModel (_type_): _description_
    """
    absolute:float
    change:float
    message:str
