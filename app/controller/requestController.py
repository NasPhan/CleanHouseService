from flask import Blueprint, jsonify, request
from app.model.account import Account
from app.model.request import Request
from app.model.role import Role
#from app.service.accountService import AccountService
from app.service.roleService import RoleService
from app import conn
import re
import jwt

api_request = Blueprint('requestController', __name__)
session = conn.Session()
#request_service = RequestService(session)
role_service = RoleService(session)

@api_request.route('/get/id', methods = ['GET'])
def get_requests():
    requests_db = session.query(Request).all()

    requests_list = []
    for request in requests_db:
        request_dict = {
            'customerId'      : request.customerId,
            'cleanerId'       : request.cleanerId,
            'requestDetailId' : request.requestDetailId,
            'createDate'      : request.createDate,
        }
        requests_list.append(request_dict)
    return jsonify(requests_list)