from sqlalchemy import Column, Integer, TEXT, ForeignKey, DATETIME
from app.model.user import Users
from app.model.requestDetail import requestDetail
from sqlalchemy.orm import relationship
from app.model import Base;

class Request(Base):
    __tablename__   = 'request'
    id              = Column(Integer, primary_key=True,autoincrement=True)
    customerId      = Column(ForeignKey("user.id"))
    cleanerId       = Column(ForeignKey("user.id"))
    requestDetailId = Column(ForeignKey("requestDetail.id"))
    createDate      = Column(DATETIME)
    user            = relationship("User", back_populates="request")
    requestDetail   = relationship("requestDetail", back_populates="request")

    def __init__(seft, customerId, cleanerId, requestDetailId, createDate):
        seft.customerId      = customerId
        seft.cleanerId       = cleanerId
        seft.requestDetailId = requestDetailId
        seft.createDate      = createDate
    
    def to_json(seft):
        return {
            'customerId'      : Users.to_json(seft.customerId),
            'cleanerId'       : Users.to_json(seft.cleanerId),
            'requestDetailId' : requestDetail.to_json(seft.requestDetailId),
            'createDate'      : seft.createDate,
        }
