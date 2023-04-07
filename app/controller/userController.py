from flask import Blueprint, jsonify, request
from app.model.account import Account
from app.model.user import Users
from app.model.role import Role
from app.service.accountService import AccountService
from app.service.userService import UserService
from app.service.roleService import RoleService
from app import conn
import re
import jwt

api_user = Blueprint('userController', __name__)
session = conn.Session()
user_service = UserService(session)
role_service = RoleService(session)

@api_user.route('/user/update', methods = ['PUT'])
def update_user():
    data = request.get_json()
    firstName = data['firstName']
    lastName  = data['lastName']
    phone     = data['phone']
    age       = data['age']
    gender    = data['gender']
    address   = data['address']
    avatar    = data['avatar']
    id = data['id']
    print(id)
    try:
        user = user_service.update_user(firstName, lastName, phone, age, gender, address, avatar, id)
        # payload      = {'username': Account.to_json(user)}
        # secret_key   = 'secret_key'
        # token        = jwt.encode(payload, secret_key, algorithm = 'HS256')
        response     = jsonify({'message': 'Cập nhật thông tin thành công!'})
        # token_string = token.encode("utf-8").decode("utf-8")
        # response.set_cookie('token', token_string, httponly = True, secure = True)
        return response
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
