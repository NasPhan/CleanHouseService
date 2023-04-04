from sqlalchemy import Column, Integer,TEXT, ForeignKey
from app.model import Base;
from app.model.role import Role


class Account(Base):
    __tablename__ = 'account'
    id        = Column(Integer, primary_key=True,autoincrement=True)
    userName  = Column(TEXT)
    passWord  = Column(TEXT)
    roleId    = Column(ForeignKey("role.id"))
    userId    = Column(ForeignKey("user.id"))

    def __init__(seft, userName, passWord, roleId, userId):
        seft.userName  = userName
        seft.passWord  = passWord
        seft.roleId    = roleId
        seft.userId    = userId
    
    def to_json(seft):
        return {
            'userName'  : seft.userName,
            'passWord'  : seft.passWord,
            'roleId'    : Role.to_json(seft.roleId),
        }
