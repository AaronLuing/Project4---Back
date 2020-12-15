from flask import Flask

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class
# This starts the website
app = Flask(__name__)

# the default url ends in / ("website-url/")
@app.route('/')
def index():
  return 'Hello World!'

# Run the app when the program starts
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)