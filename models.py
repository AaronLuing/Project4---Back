# from peewee import *
# import datetime
# from flask_login import UserMixin
# import os
# import urllib.parse as urlparse

# urlparse.uses_netloc.append('postgres')
# url = urlparse.urlparse(os.environ['DATABASE_URL'])
# # for your config
# DATABASE_INFO = {
#     'engine': 'peewee.PostgresqlDatabase',
#     'name': url.path[1:],
#     'password': url.password,
#     'host': url.hostname,
#     'port': url.port,
#     'user': url.user
# }

# DATABASE = PostgresqlDatabase(DATABASE_INFO['name'],password=DATABASE_INFO['password'],
#   port=DATABASE_INFO['port'], host=DATABASE_INFO['host'], user=DATABASE_INFO['user'])
import os
import urllib.parse as urlparse
import psycopg2
from flask import Flask
from flask_peewee.db import Database
if 'HEROKU' in os.environ:
    DEBUG = False
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }
else:
    DEBUG = True
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': 'framingappdb',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432 ,
        'threadlocals': True
    }
app = Flask(__name__)
app.config.from_object(__name__)
db = Database(app)

class Users(UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()

  class Meta:
    database = DATABASE

# field types learned from:
# http://docs.peewee-orm.com/en/latest/peewee/models.html

class Expense(Model):
  name = CharField()
  category = CharField()
  amount = IntegerField()
  userid = CharField()
  # profile = ForeignKeyField(Users, backref='expenses')
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Users, Expense], safe=True)
  print("TABLES Created")
  DATABASE.close()