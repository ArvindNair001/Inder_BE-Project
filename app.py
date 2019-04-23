from flask import Flask
import flask
import routes
app = Flask(__name__, static_url_path='/static')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

from routes import *;

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)

'''
    debug = True will ensure that you dont have to restart the server after 
    every change.. Thank me later ;-) DCOMFORT...
'''