import json
import pickle

from google.cloud.storage import Client
import torch
from torch import nn, Tensor, tensor
import numpy as np
from sklearn.experimental import enable_halving_search_cv  # noqa

from app.model.prediction import PredictionRequest, PredictionResponse
from app.config import settings


class PredictorNN(nn.Module):
    """Input is 3 days of sentiment and stock values.
    Output is next day stock value.
    """
    INPUT = 6
    
    def __init__(self) -> None:
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(self.INPUT, self.INPUT*8),
            nn.ReLU(),
            nn.Linear(self.INPUT*8, self.INPUT*4),
            nn.ReLU(),
            nn.Linear(self.INPUT*4, 1),
            nn.ReLU()
        )

    def forward(self, x):
        return self.fc(x)

    def load(self, file) -> bool:
        try:
            self.load_state_dict(torch.load(file))
            self.eval()
            return True
        except:
            return False

class PredictionService:
    """PredictionService
    """

    DATA_LENGTH = 3
    sentiment_name = 'LogisticRegression'
    predictor_name = 'PredictorNN'
    sentiment_model = None
    prediction_model = None
    features = None
    is_ok = False

    def __init__(self) -> None:
        """Init PredictionService
        """
        # Initialize google storage 
        if settings.CREDENTIALS_JSON:
            client = Client.from_service_account_json(settings.CREDENTIALS_JSON)
        else:
            client = Client()
        bucket = client.get_bucket(f'{settings.GOOGLE_CLOUD_PROJECT}.appspot.com')
        if bucket.exists():
            # Get sentiment model.
            blob = bucket.get_blob(f'predictor/{self.sentiment_name}.bin')
            if blob.exists():
                with blob.open('rb') as f:
                    self.sentiment_model,_ = pickle.load(f)
            # Get stock model.
            blob = bucket.get_blob(f'predictor/{self.predictor_name}.bin')
            if blob.exists():
                with blob.open('rb') as f:
                    self.prediction_model = PredictorNN()
                    self.prediction_model.load(f)
            # Get text features
            blob = bucket.get_blob('predictor/features.json')
            if blob.exists():
                with blob.open('rb') as f:
                    self.features = json.load(f)
        self.is_ok = self.features and self.sentiment_model and self.prediction_model

    def predict(self, req:PredictionRequest) -> PredictionResponse:
        """Make prediction based on PredictionRequest.
        Args:
            req (PredictionRequest): Request with PredictionService.DATA_LENGTH days of data.
        Returns:
            PredictionResponse: Prediction
        """
        if self.is_ok:
            value = self.prediction_model(self.get_data(req.news,req.stock))
            return PredictionResponse(value=value, message='Ok')
        else:
            return PredictionResponse(value=0, message='Not initialized')

    def get_data(self, news:list[str], stock:list[float]) -> Tensor:
        """Get prediction data as a tensor.

        Args:
            news (list[str]): _description_
            stock (list[float]): _description_

        Returns:
            nn.tensor: prediction data
        """
        X_data = np.zeros(self.DATA_LENGTH*2, dtype=np.float32)
        for i in range(self.DATA_LENGTH):
            X_data[i] = stock[i]
            X_data[i + self.DATA_LENGTH] = self.get_sentiment(news[i])
        
        result = tensor(X_data, dtype=torch.float32)
        return result
    
    def get_sentiment(self, sentence:str) -> float:
        """Get sentiment prediction for text.

        Args:
            sentence (str): text

        Returns:
            float: score
        """
        # sentence histogram
        wmap = {}
        for word in sentence.lower().split():
            if word in wmap:
                wmap[word] += 1
            else: wmap[word] = 1
        # feature array
        feat = np.zeros(len(self.features), dtype=np.float32)
        # populate array
        for i,word in enumerate(self.features):
            if word in wmap:
                feat[i] = wmap[word]
        # classify
        result = self.sentiment_model.predict([feat])[0]
        return result

__all__ = ('PredictionService', 'PredictionRequest', 'PredictionResponse')
