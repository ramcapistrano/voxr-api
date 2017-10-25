from flask import Flask, jsonify, request
from app.users import UserResource
from app.users.model import User
from passlib.hash import bcrypt_sha256

app = Flask(__name__, static_folder='app/static')
app.register_blueprint(UserResource)


@app.route("/voxr/api/")
def home():
    return "Welcome to Voxr API!"


@app.route("/voxr/api/login", methods=['POST'])
def login():
    try:
        username = request.json["username"]
        password = request.json["password"]

        user = User.query.filter_by(username=username).first()
        if user is not None:
            is_password_matched = bcrypt_sha256.verify(password, user.password)
            if is_password_matched is True:
                print 'Login successful'
                return jsonify(user.serialize), 200
            else:
                return jsonify('Invalid credentials'), 401

        return jsonify('User do not exist'), 400
    except KeyError as ke:
        return jsonify('Attribute ' + ke.args[0] + ' missing!'), 400


if __name__ == '__main__':
    # app.run(debug=True, host='localhost', port=5001, threaded=True)
    app.run(debug=True, host='0.0.0.0', port=9000, threaded=True)