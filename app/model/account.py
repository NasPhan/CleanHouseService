from sqlalchemy import Column, Integer,TEXT, ForeignKey
from app.model import Base;
from sqlalchemy.orm import relationship
from app.model.role import Role


class Account(Base):
    __tablename__ = 'account'
    id        = Column(Integer, primary_key=True,autoincrement=True)
    userName  = Column(TEXT)
    passWord  = Column(TEXT)
    roleId    = Column(ForeignKey("role.id"))
    role      = relationship("Role", back_populates="account")
    user      = relationship("Users", back_populates="account")

    def __init__(seft, userName, passWord, roleId):
        seft.userName  = userName
        seft.passWord  = passWord
        seft.roleId    = roleId
    
    def to_json(seft):
        return {
            'userName'  : seft.userName,
            'passWord'  : seft.passWord,
            'roleId'    : Role.to_json(seft.roleId),
        }
