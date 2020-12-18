# from flask import Flask, jsonify, g
# from flask_cors import CORS
# from flask_login import LoginManager
# from peewee import *
# import models
# from resources.expenses import expense
# from resources.users import user

# login_manager = LoginManager()

# DEBUG = True
# PORT = 8000

# # Initialize Flask
# app = Flask(__name__)

# app.secret_key = "kljahfiruehf"
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(userid):
#   try:
#     return models.Users.get(models.Users.id == userid)
#   except models.DoesNotExist:
#     return None

# # Logic for db connection
# @app.before_request
# def before_request():
#   g.db = models.DATABASE
#   g.db.connect()

# @app.after_request
# def after_request(response):
#   g.db.close()
#   # return response
#   header = response.headers
#   header['Access-Control-Allow-Origin'] = '*'
#   return response

# CORS(expense, origins='*', supports_credentials=True)
# CORS(user, origins='*', supports_credentials=True)

# app.register_blueprint(expense, url_prefix='/api/v1/budget')
# app.register_blueprint(user, url_prefix='/user')

# @app.route('/')
# def index():
#     return "<h1>Welcome to the server !!</h1>"

# @app.route('/surprise')
# def surprise():
#   return'<h1>SURPRISE!!!</h1>'

# # Run the app when the program starts
# if __name__ == '__main__':
#   models.initialize()
#   app.run(debug=DEBUG, port=PORT)

from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

import models
from resources.expenses import expense
from resources.users import user

login_manager = LoginManager()

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class
# This starts the website
app = Flask(__name__)

app.secret_key = "kljahfiruehf"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
  try:
    return models.Users.get(models.Users.id == userid)
  except models.DoesNotExist:
    return None

# Logic for our database connection
@app.before_request
def before_request():
  """Connect to the database before each request"""
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(response):
  """Close the db connection after each request"""
  g.db.close()
  return response

CORS(expense, origins='*', supports_credentials=True)
CORS(user, origins='*', supports_credentials=True)

app.register_blueprint(expense, url_prefix='/api/v1/budget')
app.register_blueprint(user, url_prefix='/user')

# the default url ends in / ("website-url/")
@app.route('/')
def index():
  return 'Hello World!'

# Run the app when the program starts
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)