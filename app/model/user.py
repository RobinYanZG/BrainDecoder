import datetime
from peewee import CharField, DateTimeField, AutoField

from app.model.base_model import BaseModel


class User(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'chat_user'
        