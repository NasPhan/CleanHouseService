from flask import Blueprint, jsonify, request
from app.model.account import Account
from app.model.user import Users
from app.model.role import Role
from app import conn

api_account = Blueprint('accountController', __name__)
session = conn.Session()

@api_account.route('/login', methods = ['POST'])
def check_acc():
    data = request.get_json()
    userName = data['userName']
    passWord = data['passWord']
    user = session.query(Account).filter(Account.userName == userName, Account.passWord == passWord).first()
    if user:
        return jsonify({'mesage' : 'Login success', 'role' : user.roleId})
    else:
        return jsonify({'message' :'Invalid userName or passWord' })
    

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
