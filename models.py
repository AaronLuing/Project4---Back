from peewee import *
import datetime

DATABASE = PostgresqlDatabase('budget')

class Expense(Model):
  name = CharField()
  category = CharField()
  amount = CharField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Expense], safe=True)
  print("TABLES Created")
  DATABASE.close()