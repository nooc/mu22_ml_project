from os import environ

from google.cloud.storage import Client

from app.model.prediction import PredictionRequest, PredictionResponse


class PredictionService:
    """PredictionService
    """

    def __init__(self) -> None:
        """Init PredictionService
        """
        if 'CRED_JSON' in environ:
            client = Client.from_service_account_json(environ['CRED_JSON'])
        else:
            client = Client()
        
        # TODO load ML models from bucket

    def predict(self, input:PredictionRequest) -> PredictionResponse:
        """Make prediction.

        Args:
            input (PredictionRequest): Request

        Returns:
            PredictionResponse: Prediction
        """

        # TODO prediction code here

        return PredictionResponse(absolute=0.14, change=0.01)
