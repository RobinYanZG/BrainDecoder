from app.core.chat_management import ChatManagement

class ChatService:
        
    def __init__(self, chat_management: ChatManagement):
        self.chat_management = chat_management
        
    def chat(self, query: str, history: list, vector_index: str) -> tuple:
        return self.chat_management.chat_with_store(query, history, vector_index)
    