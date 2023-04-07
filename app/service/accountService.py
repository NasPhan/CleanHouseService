from flask import Blueprint, jsonify, request
from app.model.account import Account
from unidecode import unidecode
import re

class AccountService():
    def __init__(self, session):
        self.session = session

    def check_account(seft, userName, passWord):
        account = seft.session.query(Account).filter(Account.userName == userName, Account.passWord == passWord).first()
        if not account:
            raise ValueError ('Sai tên đăng nhập hoặc mật khẩu')
        return account
    
    def validate_user(selt, userName):
        if len(userName) < 6 :
            raise ValueError('Tên đăng nhập phải lớn hơn 5 ký tự')
        
        if not re.match('^[a-zA-Z0-9_]+$', userName):
            raise ValueError('Tên đăng nhập chỉ chứa ký tự hoặc chữ số')
        
        # if not all(c.isalpha() and unidecode(c) in 'abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOQPRSTUWXYZ0123456789' for c in userName):
        #     raise  ValueError('Không chứa ký tự hoặc chữ số')
    
    def validate_passWord(self, passWord):
        if len(passWord) < 8:
            raise ValueError('Mật khẩu phải có ít nhâts 8 kí tự')
        if not any(c.isupper() for c in passWord):
            raise ValueError('Mật khẩu mới phải chứa ít nhất một ký tự in hoa')
        if not any(c.islower() for c in passWord):
            raise ValueError('Mật khẩu mới phải chứa ít nhất một ký tự in thường')
        if not any(c.isdigit() for c in passWord):
            raise ValueError('Mật khẩu mới phải chứa ít nhất một số')
        account = self.session.query(Account).filter( Account.passWord == passWord).first()
        if not account:
            raise ValueError('Sai mật khẩu')
        return account
        
    def crete_account(selt, userName, passWord, role):
        check_account = selt.session.query(Account).filter(Account.userName == userName).first()
        if check_account:
            raise ValueError ('Tên đăng nhập đã tồn tại')
        new_account = Account(userName, passWord, role)
        selt.session.add(new_account)
        selt.session.commit()
        return new_account
    
    def change_passWord(selt, userName, oldPassWord, newPassWord):
        account = selt.session.query(Account).filter(Account.userName == userName, Account.passWord == oldPassWord).first()
        if not account:
            raise ValueError ('Sai tên đăng nhập hoặc mật khẩu')    
        Account.passWord = newPassWord
        selt.session.commit()
        return account
        
    
    def validate_account(selt, userName, passWord):
        selt.validate_user(userName)
        selt.validate_passWord(passWord)
        account = selt.session.query(Account).filter(Account.userName == userName, Account.passWord == passWord).first()
        if not account:
            raise ValueError('Sai tên đăng nhập hoặc mật khẩu')
        return account