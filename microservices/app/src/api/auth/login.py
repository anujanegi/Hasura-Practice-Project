import requests
import json
from api import api

@api.route('/signup', methods=['POST'])
def signin():
    # This is the url to which the query is made
    url = "https://auth.analogically97.hasura-app.io/v1/signup"

    username = request.json.get("username", None)
    password = request.json.get("pswd", None)

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
