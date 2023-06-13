from app.model.conversation import Conversation
from app.model.message import Message

class HistoryService:
        
    def create(self, user_id, titile) -> tuple:
        conversation = Conversation(user_id=user_id, titile=titile)
        return conversation.save()
    
    def get_conversation_by_id_and_user(self, conversation_id, user_id):
        conversation = Conversation.get(Conversation.id == conversation_id)
        return conversation
    
    def check_coversation_exists(self, conversation_id, user_id):
        conversation = Conversation.get_or_none(Conversation.id == conversation_id and Conversation.user == user_id)
        return conversation is not None
    
    def get_history(self, conversation_id):
        messages = []
        list = Message.select().where(Message.conversation == conversation_id)
        for m in list:
            messages.append([m.query, m.answer])
        return messages
    