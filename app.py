import base64
import os
import jsonpickle
from flask import Flask, render_template, request

app = Flask(__name__)


class User(object):
    def __init__(self, user):
        self.username = user


@app.route('/')
def enter():  # put application's code here
    if os.path.exists('../tmp/flag.txt'):
        user_cookie = request.cookies.get('user')
        #decode base64
        if user_cookie:
            try:
                user = jsonpickle.decode(base64.b64decode(user_cookie))
                if user.username == 'admin':
                    return render_template('admin.html')
                else:
                    return render_template('index.html')
            except Exception as e:
                response = app.make_response(render_template('index.html'))
                response.delete_cookie('user')
                return response
        # create cookie
        guest = User('guest')
        encoded = jsonpickle.encode(guest)
        b64 = base64.b64encode(encoded.encode())
        response = app.make_response(render_template('index.html'))
        response.set_cookie('user', str(b64))
        return response
    else:
        return render_template('flag.html')


if __name__ == '__main__':
    app.run()
