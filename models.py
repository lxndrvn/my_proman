from peewee import *

db = PostgresqlDatabase('lxndrvn', user='lxndrvn')


class BaseModel(Model):
    class Meta:
        database = db


class Board(BaseModel):
    title = CharField()


class Card(BaseModel):
    title = CharField()
    board = ForeignKeyField(Board)
    status = CharField()

