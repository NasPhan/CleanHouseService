from app.model.role import Role
from sqlalchemy import func

class RoleService():
    def __init__(self, session):
        self.session = session
    
    def check_role(seft, role):
        role_check = seft.session.query(Role).filter(Role.id == role).first()
        if not role_check:
            raise ValueError('Role does not exit')