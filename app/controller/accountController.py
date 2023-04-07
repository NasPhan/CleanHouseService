from flask import Blueprint, jsonify, request
from app.model.account import Account
from app.model.user import Users
from app.model.role import Role
from app.service.accountService import AccountService
from app.service.roleService import RoleService
from app import conn
import re
import jwt


api_account = Blueprint('accountController', __name__)
session = conn.Session()
account_service = AccountService(session)
role_service = RoleService(session)

@api_account.route('/login', methods = ['POST'])
def check_acc():
    data     = request.get_json()
    userName = data['userName']
    passWord = data['passWord']
    try:
        user         = account_service.check_account(userName, passWord)
        payload      = {'role': user.roleId}
        secret_key   = 'secret_key'
        token        = jwt.encode(payload, secret_key, algorithm = 'HS256')
        response     = jsonify({'message': 'Đăng nhập thành công!', "role": Role.to_json(user.role)})
        token_string = token.encode("utf-8").decode("utf-8")
        response.set_cookie('token', token_string, httponly = True, secure = True)
        return response
    except ValueError as e:
        return jsonify({'message': str(e)})
    
    
@api_account.route('/register', methods = ['POST'])
def register():
    data     = request.get_json()
    userName = data['userName']
    passWord = data['passWord']
    role     = data['role']
    try:
        user = account_service.crete_account(userName, passWord, role)
        user = account_service.validate_account(userName, passWord)
        payload      = {'role': user.roleId}
        secret_key   = 'secret_key'
        token        = jwt.encode(payload, secret_key, algorithm = 'HS256')
        response     = jsonify({'message': ' Đăng ký tài khoản thành công!'})
        token_string = token.encode("utf-8").decode("utf-8")
        response.set_cookie('token', token_string, httponly = True, secure = True)
        return response
    except ValueError as e:
        return jsonify({'message': str(e)})


@api_account.route('/changepass', methods = ['PUT'])
def change_passWord():
    data = request.get_json()
    userName = data['userName']
    oldPassWord = data['oldPassWord']
    newPassWord = data['newPassWord'] 
    try:
        account = account_service.change_passWord(userName, oldPassWord, newPassWord)
        account = account_service.validate_passWord(newPassWord)
        payload      = {'role': account.roleId}
        secret_key   = 'secret_key'
        token        = jwt.encode(payload, secret_key, algorithm = 'HS256')
        response     = jsonify({'message': 'Đổi mật khẩu thành công!', "role": Role.to_json(account.role)})
        token_string = token.encode("utf-8").decode("utf-8")
        response.set_cookie('token', token_string, httponly = True, secure = True)
        return response
    except ValueError as e:
        return jsonify({'message': str(e)})


@api_account.route('/get', methods = ['GET'])
def get_users():
    users_db = session.query(Users).all()

    users_list = []
    for user in users_db:
        user_dict = {
            'firstName' : user.firstName,
            'lastName'  : user.lastName,
            'phone'     : user.phone,
            'age'       : user.age,
            'gender'    : user.gender,
            'address'   : user.address,
            'avatar'    : user.avatar
        }
        users_list.append(user_dict)
    return jsonify(users_list)
