from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.name


def create_tables():
    with db:
        db.create_tables([Person])