"""
Primary FastPI application
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import api_routes
from .config import settings

def create_app():
    '''Initialize FastAPI app'''
    app = FastAPI(
        title = settings.TITLE,
        description = settings.DESCRIPTION,
        openapi_url = settings.OPENAPI_URL,
        docs_url = settings.DOCS_URL,
        redoc_url = None)

    # Enable CORS via middleware
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    app.include_router(api_routes)

    return app


application = create_app()
