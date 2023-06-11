from app.core.chat_management import ChatManagement

class ChatService:
        
    def __init__(self, chat_management: ChatManagement):
        self.chat_management = chat_management
        
    def chat(self, query: str, history: list) -> tuple:
        return self.chat_management.chat(query, history)