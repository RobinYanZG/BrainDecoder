from fastapi import FastAPI
from app.helper.logger import logger
from app.api.routes import router as api_router
from app.middleware.http_logger import http_logger


def create_app() -> FastAPI:
    logger.info("*************************Create App*****************************")

    app = FastAPI()
    
    app.middleware("http")(http_logger)
    
    app.include_router(api_router, prefix="/api")
    return app
