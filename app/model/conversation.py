import datetime
from app.model.base_model import BaseModel
from peewee import CharField, DateTimeField, AutoField, ForeignKeyField
from app.model.user import User


class Conversation(BaseModel):
    id = AutoField(primary_key=True)
    user = ForeignKeyField(User)
    title = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'chat_conversation'
