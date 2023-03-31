from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE = 'Stock movement prediction service'
    DESCRIPTION = 'Predict stock movement by finantial news.'
    OPENAPI_URL = '/api-spec/openapi.json'
    DOCS_URL = '/api-doc'

    LOCAL_RUN: Optional[bool] = False

    GOOGLE_CLOUD_PROJECT: Optional[str] = None
    GAE_APPLICATION: Optional[str] = None
    GAE_DEPLOYMENT_ID: Optional[str] = None
    GAE_INSTANCE: Optional[str] = None
    TASK_QUEUE_NAME: Optional[str] = "default"
    GAE_REGION: Optional[str] = None
    CREDENTIALS_JSON: Optional[str] = None

settings = Settings()
