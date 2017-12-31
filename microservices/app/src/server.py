from src import app
from flask import render_template
import requests
import json
# from flask import jsonify


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    url = "https://auth.analogically97.hasura-app.io/v1/signup"

    username = request.form['username']
    password = request.form['pswd']

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": "anuja",
            "password": "anuja123"
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    print resp.content
    return "done"
