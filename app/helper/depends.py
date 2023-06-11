
from app.core.chat_management import chat_management
from app.service.chat_service import ChatService


def get_chat_service():
    return ChatService(chat_management)