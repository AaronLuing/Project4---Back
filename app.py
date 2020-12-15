from flask import Flask, jsonify, g
from flask_cors import CORS

import models
from resources.expenses import expense

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class
# This starts the website
app = Flask(__name__)

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

CORS(expense, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(expense, url_prefix='/api/v1/budget')
# the default url ends in / ("website-url/")
@app.route('/')
def index():
  return 'Hello World!'

# Run the app when the program starts
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)