from fastapi import FastAPI
from app.helper.logger import logger
from app.api.routes import router as api_router
from app.middleware.http_logger import http_logger
from app.model.conversation import Conversation
from app.model.message import Message
from app.model.user import User
from db.db import db


def create_app() -> FastAPI:
    logger.info("*************************Create App*****************************")

    app = FastAPI()
    
    app.middleware("http")(http_logger)
    
    app.include_router(api_router, prefix="/api")
    
    @app.on_event("startup")
    async def startup():
        db.create_tables([User, Conversation, Message])

    @app.on_event("shutdown")
    async def shutdown():
        db.close()
    
    return app
