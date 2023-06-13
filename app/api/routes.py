from fastapi import APIRouter
from app.api import chat_controller
from app.api import user_controller

router = APIRouter()

router.include_router(
    chat_controller.router,
    tags=["chat"],
    prefix="/chat"
)

router.include_router(
    user_controller.router,
    tags=["user"],
    prefix="/user"
)
