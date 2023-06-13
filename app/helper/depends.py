from app.core.chat_management import chat_management
from app.service.user_service import UserService
from app.service.chat_service import ChatService
from app.service.history_service import HistoryService


def get_chat_service():
    return ChatService(chat_management)

def get_user_service():
    return UserService()

def get_history_service():
    return HistoryService()