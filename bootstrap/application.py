from fastapi import FastAPI
from app.helper.logger import logger
from app.api.routes import router as api_router

# from app.providers import app_provider
# from app.providers import logging_provider
# from app.providers import handle_exception
# from app.providers import route_provider


def create_app() -> FastAPI:
    logger.info("*************************Create App*****************************")

    app = FastAPI()
    app.include_router(api_router, prefix="/api")
    return app
