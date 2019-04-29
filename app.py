from flask import Flask
# from routes import *


app = Flask(__name__, static_url_path='/static')

from routes import *

# @app.route('/')
# def index():
#     return 'INDEX'

if __name__ == '__main__':
    app.run(debug=True)
