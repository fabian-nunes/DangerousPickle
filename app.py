import base64
import os
import jsonpickle
from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class User(object):
    def __init__(self, user):
        self.username = user


@app.route('/')
def index():  # put application's code here
    if os.path.exists('../tmp/flag.txt'):
        return render_template('index.html')
    else:
        return render_template('flag.html')


@app.route('/access')
def access():
    code = request.args.get('code')
    if code:
        try:
            user = jsonpickle.decode(base64.b64decode(code))
            if user.username == 'guest' or user.username == 'worker':
                return Response(status=200, response='Hello ' + user.username)
            else:
                return Response(status=403, response='Error: Unauthorized')
        except Exception as e:
            return Response(status=500, response='Error: ' + str(e))
    else:
        return Response(status=400, response='Error: code is required')


if __name__ == '__main__':
    app.run()
