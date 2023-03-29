from typing import Any

from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from app.service.prediction_service import (PredictionRequest,
                                            PredictionResponse,
                                            PredictionService)

from .dependencies import predictor_dep

# Init FastAPI router for API endpoints
api_routes = APIRouter()


@api_routes.get('/', include_in_schema=False)
def redirect_to_docs():
    """Redirect to API docs when at site root"""
    return RedirectResponse('/api-doc')


@api_routes.post(
    '/predict',
    description='Make prediction based on input data.',
    response_model=PredictionResponse
)
async def make_prediction(
    data: PredictionRequest,
    predictor:PredictionService = Depends(predictor_dep)
) -> Any:
    """Predict next day stock movement based on PredictionRequest.

    Args:
        data (PredictionRequest): Prediction data

    Returns:
        Any: PredictionResponse
    """
    return predictor.predict(data)
