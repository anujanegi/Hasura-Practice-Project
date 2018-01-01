from src import app
from flask import render_template, request, json
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
    pswd = request.form['pswd']

    # This is the url to which the query is made
    url = "https://auth.analogically97.hasura-app.io/v1/signup"

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": username,
            "password": pswd
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    print(resp.content)
    return (resp.content)

@app.route("/signin", methods=['POST'])
def signin():
    username = request.form['username']
    pswd = request.form['pswd']

    # This is the url to which the query is made
    url = "https://auth.analogically97.hasura-app.io/v1/signup"
    # This is the url to which the query is made
    url = "https://auth.analogically97.hasura-app.io/v1/login"

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": "nsmith",
            "password": "js@hasura"
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    print(resp.content)
    return (resp.content)
