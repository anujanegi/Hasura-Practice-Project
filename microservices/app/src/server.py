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

@views.route('/signup', methods=['POST'])
def signup():
    #API URL
    url = request.url_root + url_for('api.login')[1:]
    try:
        data = json.loads(json.dumps(request.form))
        r = requests.post(url, json = data)
        res = r.json()
        if res["code"] == 200:
            #Set session for this blueprint
            session["user-token"] = res["args"]
            return redirect('/')
        else:
            return redirect('/')
    except Exception as e:
        return str(e)

# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
