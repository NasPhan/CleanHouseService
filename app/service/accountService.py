from app.model.account import Account
from unidecode import unidecode
import re

class AccountService():
    def __init__(self, session):
        self.session = session

    def check_account(seft, userName, passWord):
        user = seft.session.query(Account).filter(Account.userName == userName, Account.passWord == passWord).first()
        if not user:
            raise ValueError ('Sai tên đăng nhập hoặc mật khẩu')
        return user
    
    def validate_user(selt, userName):
        if len(userName) < 6 :
            raise ValueError('Tên đăng nhập phải lớn hơn 5 ký tự')
        
        if not re.match('^[a-zA-Z0-9_]+$', userName):
            raise ValueError('Không chứa ký tự hoặc chữ số')
        
        # if not all(c.isalpha() and unidecode(c) in 'abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOQPRSTUWXYZ0123456789'):
        #     raise  ValueError('Không chứa ký tự hoặc chữ số')
    
    def validate_passWord(self, passWord):
        if len(passWord) < 6 or len(passWord) > 12:
            raise ValueError('Mật khẩu có từ 6 đến 12 kí tự')
        
    def crete_account(selt, userName, passWord, role):
        pass