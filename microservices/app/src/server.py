from src import app
from flask import render_template, json, requests
from flask import jsonify


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup", methods=['POST'])
def signup():

    return "done"
