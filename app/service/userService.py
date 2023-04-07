from flask import Blueprint, jsonify, request
from app.model.user import Users
from app.model.account import Account
from unidecode import unidecode
import re

class UserService():
    def __init__(self, session):
        self.session = session

    def update_user(self, firstName, lastName, phone, age, gender, address, avatar, id):
        user = self.session.query(Users).filter(Users.id == id).first()
        if not user:
            raise ValueError('Tài khoản không tồn tại')
        user.firstName = firstName
        self.session.commit()
        return user
