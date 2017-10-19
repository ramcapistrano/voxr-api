from flask import jsonify, request, Blueprint
from passlib.hash import bcrypt_sha256
from sqlalchemy.exc import IntegrityError

import dao as user_dao
from app.records import dao as record_dao
from app.records.model import Record, SessionDB as record_sessionDB
from model import User, SessionDB as user_sessionDB
from validator import validate
from app.utils import upload_wav_file, generate_new_file_path
from app.open_vokaturi import extract_emotions

UserResource = Blueprint('UserResource', __name__)


# Create User
@UserResource.route("/voxr/api/users", methods=['POST'])
def create_user():
    try:
        username = request.json["username"]
        password = request.json["password"]
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        email = request.json["email"]

        val = validate(username, password, first_name, last_name, email)
        if val is not None:
            return jsonify(val[0]), val[1]

        # Encypt password
        encrypted_password = bcrypt_sha256.encrypt(password)

        user = User(username, encrypted_password, first_name, last_name, email)

        user_dao.save(user)

        return jsonify('User successfully created'), 201

    except KeyError as ke:
        user_sessionDB.rollback()
        return jsonify('Attribute ' + ke.args[0] + ' missing!'), 400

    except IntegrityError as ie:
        user_sessionDB.rollback()
        error = ie.args[0].split("\"")
        print error[1]
        return jsonify(error[1]), 500


# Get User
@UserResource.route('/voxr/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    temp_user = user_dao.get(user_id)
    if temp_user is None:
        return jsonify('User id doesn\'t exists!'), 404

    else:
        user = temp_user.serialize
        return jsonify(user), 200


# Create and Get User Records
@UserResource.route('/voxr/api/users/<int:user_id>/records', methods=['GET', 'POST'])
def user_records(user_id):
    temp_user = user_dao.get(user_id)
    if temp_user is None:
        return jsonify('User id doesn\'t exists!'), 404
    else:
        user = temp_user.serialize
        if request.method == 'GET':
            records = record_dao.get_all(user_id)
            return jsonify(records), 200
        elif request.method == 'POST':
            try:
                wav_base64 = request.json["wav_file"]
                file_path = upload_wav_file(wav_base64, user['username'])
                new_file_path = generate_new_file_path(user['username'], file_path)
                emotions = extract_emotions(file_path)
                neutrality = emotions['neutrality']
                happiness = emotions['happiness']
                sadness = emotions['sadness']
                anger = emotions['anger']
                fear = emotions['fear']

                record = Record(user['id'], neutrality, happiness, sadness, anger, fear, new_file_path)
                record_dao.save(record)
                return jsonify(emotions), 201

            except KeyError as ke:
                record_sessionDB.rollback()
                return jsonify('Attribute ' + ke.args[0] + ' missing!'), 400

            except IntegrityError as ie:
                record_sessionDB.rollback()
                error = ie.args[0].split("\"")
                print error[1]
                return jsonify(error[1]), 500


# Get User Record
@UserResource.route('/voxr/api/users/<int:user_id>/records/<int:record_id>', methods=['GET', 'DELETE'])
def user_record(user_id, record_id):
    temp_user = user_dao.get(user_id)
    if temp_user is None:
        return jsonify('User id doesn\'t exists!'), 404
    else:
        if request.method == 'GET':
            record = record_dao.get(user_id, record_id)
            if record is not None:
                return jsonify(record.serialize), 200
            else:
                return jsonify('Record id doesn\'t exists!'), 404
        elif request.method == 'DELETE':
            is_updated = record_dao.update(user_id, record_id)
            if is_updated is True:
                return jsonify('Record has been removed'), 202
            else:
                return jsonify('Record id doesn\'t exists!'), 404
