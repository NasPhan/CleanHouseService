from flask import Blueprint, jsonify, request
from app.model.account import Account
from app.model.requestDetail import RequestDetail
from app.model.role import Role
#from app.service.accountService import AccountService
from app.service.roleService import RoleService
from app import conn
import re
import jwt

api_requestDetail = Blueprint('requestDetailController', __name__)
session = conn.Session()
#request_service = RequestService(session)
role_service = RoleService(session)

@api_requestDetail.route('/get', methods = ['GET'])
def get_requestDetails():
    requestDetails_db = session.query(RequestDetail).all()

    requestDetails_list = []
    for requestDetail in requestDetails_db:
        requestDetail_dict = {
            'name'      : requestDetail.name,
            'info'      : requestDetail.info,
            'status'    : requestDetail.status,
            'comment'   : requestDetail.comment,
            'startTime' : requestDetail.startTime,
            'endTime'   : requestDetail.endTime,
        }
        requestDetails_list.append(requestDetail_dict)
    return jsonify(requestDetails_list)