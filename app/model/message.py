import datetime
from peewee import  AutoField, ForeignKeyField, TextField, DateTimeField, CharField
from app.model.base_model import BaseModel
from app.model.conversation import Conversation
from app.model.user import User


class Message(BaseModel):
    id = AutoField(primary_key=True)
    conversation = ForeignKeyField(Conversation)
    sender = ForeignKeyField(User)
    topic = CharField()
    query = TextField()
    answer = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'chat_message'
        