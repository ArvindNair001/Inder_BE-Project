import flask
from flask import Flask, url_for, render_template;
from app import app;

@app.route('/')
def index():
    return render_template('home.html');

@app.route('/process',methods=["POST"])
def execute():
    return '';