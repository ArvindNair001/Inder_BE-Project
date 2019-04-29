import flask
from flask import Flask, url_for, request, render_template,jsonify;
from werkzeug import secure_filename
import os
from app import app
from tester import tester
import time

# print(os.getcwd())
UPLOAD_FOLDER = os.path.join(os.getcwd(),'Files')
# print(UPLOAD_FOLDER)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    print('not exists')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('home.html');

@app.route('/process',methods=['POST'])
def execute():
    req = request.get_json()
    data = req['inputData']
    timestr = time.strftime("%Y%m%d%H%M%S")
    tester(data,timestr)
    return jsonify({'sucess':True,'image_name': 'tree-'+timestr+'.jpg'}), 200, {"contentType":'application/json' }
    
@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        print(filename)
        # file.save(secure_filename(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ''
        
