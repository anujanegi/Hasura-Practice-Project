from src import app
from flask import render_template
from api import *
# from flask import jsonify


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    #API URL
    url = request.url_root + url_for('api.signup')[1:]
# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
