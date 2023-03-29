from app.service.prediction_service import PredictionService

def predictor_dep() -> PredictionService:
    return PredictionService()
