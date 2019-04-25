import flask
from flask import Flask, url_for, request, render_template,jsonify;
from werkzeug import secure_filename
import os
from app import app;

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
    if request.method == 'POST':
        data = request.form['inputdata']
        return jsonify({'data': data})
    return jsonify({'error': 'Invalid method'})
    
@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        print(filename)
        # file.save(secure_filename(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ''
        
@app.route('/jsontest',methods=['POST'])
def jsontest():
    data = request.get_json()
    name = data['name']
    age = data['age']
    return jsonify({'success': 'ok', 'name': name, 'age': age})