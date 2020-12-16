from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('budget')

class Users(UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()

  class Meta:
    database = DATABASE

class Expense(Model):
  name = CharField()
  category = CharField()
  amount = IntegerField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Expense], safe=True)
  print("TABLES Created")
  DATABASE.close()