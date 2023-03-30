from os import environ

from google.cloud.storage import Client

from app.model.prediction import PredictionRequest, PredictionResponse
from app.config import settings

from sklearn.linear_model import LogisticRegression
import pickle

class PredictionService:
    """PredictionService
    """

    logreg:LogisticRegression = None

    def __init__(self) -> None:
        """Init PredictionService
        """
        # TODO load ML models from bucket
        if settings.CREDENTIALS_JSON:
            client = Client.from_service_account_json(settings.CREDENTIALS_JSON)
        else:
            client = Client()
        bucket = client.get_bucket(f'{settings.GOOGLE_CLOUD_PROJECT}.appspot.com')
        if bucket.exists():
            blob = bucket.get_blob('predictor/LinearSVC.bin')
            if blob.exists():
                with blob.open('rb') as f:
                    self.logreg = pickle.load(f)
        

    def predict(self, req:PredictionRequest) -> PredictionResponse:
        """Make prediction.
        Args:
            req (PredictionRequest): Request
        Returns:
            PredictionResponse: Prediction
        """

        # TODO prediction code here
        return PredictionResponse(absolute=0.14, change=0.01, message='has logreg' if self.logreg else 'no logreg')


__all__ = ('PredictionService', 'PredictionRequest', 'PredictionResponse')
