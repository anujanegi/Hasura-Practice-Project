from src import app
from flask import render_template
import requests
import json


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    return username
