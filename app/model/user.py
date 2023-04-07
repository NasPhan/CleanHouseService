from sqlalchemy import Column, Enum, Integer, TEXT, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Base;

class Users(Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True,autoincrement=True)
    firstName     = Column(TEXT)
    lastName      = Column(TEXT)
    phone         = Column(TEXT)
    age           = Column(TEXT)
    gender        = Column(Enum('Nam', 'Nữ','Khác'))
    address       = Column(TEXT)
    avatar        = Column(TEXT)
    accountId     = Column(ForeignKey("account.id"))
    account       = relationship("Account", back_populates="user")

    def __init__(seft,  firstName, lassName, phone, age, gender,address , avatar, accountId):
        seft.firstName = firstName
        seft.lastName  = lassName
        seft.phone     = phone
        seft.age       = age
        seft.gender    = gender
        seft.address   = address
        seft.avatar    = avatar
        seft.accountId = accountId
    
    def to_json(seft):
        return {
            'firstName' : seft.firstName,
            'lastName'  : seft.lastName,
            'phone'     : seft.phone,
            'age'       : seft.age,
            'gender'    : seft.gender,
            'address'   : seft.address,
            'avatar'    : seft.avatar
        }