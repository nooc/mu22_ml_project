from app.service import predictor, PredictionService

def predictor_dep() -> PredictionService:
    return predictor
