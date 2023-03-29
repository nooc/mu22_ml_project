"""
Primary FastPI application
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import api_routes


def create_app():
    '''Initialize FastAPI app'''
    app = FastAPI(
        title = 'Stock movement prediction service',
        description = 'Predict stock movement by finantial news.',
        openapi_url = '/api-spec/openapi.json',
        docs_url = '/api-doc',
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
