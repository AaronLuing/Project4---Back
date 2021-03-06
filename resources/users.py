import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from flask_cors import CORS, cross_origin
from playhouse.shortcuts import model_to_dict

# first argument is the blueprints name
# second argument is it's import_name
# third argument is the url_prefix so I don't have to prefix all my urls with /user
user = Blueprint('users','user', url_prefix='/user')

@user.route('/register', methods=["POST"])
def register():
  payload = request.get_json()

  payload['email'] = payload['email'].lower()
  try:
    models.Users.get(models.Users.email == payload['email'])
    return jsonify(data={}, status={"code": 401, "message":"That username is already taken"})
  except models.DoesNotExist:
    payload['password'] = generate_password_hash(payload['password'])
    user = models.Users.create(**payload)

    login_user(user)

    user_dict = model_to_dict(user)
    print(user_dict)
    print(type(user_dict))

    del user_dict['password']

    return jsonify(data=user_dict, status={"code": 201, "message":"Successful"})


@user.route('/login', methods=["POST"])
def login():
  payload = request.get_json()
  payload['email'] = payload['email'].lower()

  print('payload:', payload)

  try:
    user = models.Users.get(models.Users.email == payload['email'])
    user_dict = model_to_dict(user)
    if(check_password_hash(user_dict['password'], payload['password'])):
      del user_dict['password']
      login_user(user)
      print(user, ' this is user')
      return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
    else:
      print("Username or password is incorrect")
      return jsonify(data={}, status={"code": 401, "message": "Incorrect login info"})
  except models.DoesNotExist:
    print("User does not exist")
    return jsonify(data={}, status={"code": 401, "message": "Incorrect login info!!"})

@user.route('/logout', methods=["GET"])
def logout():
  logout_user()
  return jsonify(data={}, status={"code": 200, "message": "Sucessfully logged out"})