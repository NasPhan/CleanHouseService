from sqlalchemy import Column, Integer, TEXT, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from app.model import Base;

class RequestDetail(Base):
    __tablename__  = 'requestDetail'
    id             = Column(Integer, primary_key=True,autoincrement=True)
    name           = Column(TEXT)
    info           = Column(TEXT)
    status         = Column(Integer)
    comment        = Column(TEXT)
    startTime      = Column(DateTime)
    endTime        = Column(DateTime)
    request        = relationship("Request", back_populates="requestDetail")

    def __init__(seft,  name, info, status, comment, startTime, endTime ):
        seft.name      = name
        seft.info      = info
        seft.status    = status
        seft.comment   = comment
        seft.startTime = startTime
        seft.endTime   = endTime
    
    def to_json(seft):
        return {
            'name'      : seft.name,
            'info'      : seft.info,
            'status'    : seft.status,
            'comment'   : seft.comment,
            'startTime' : seft.startTime,
            'endTime'   : seft.endTime,
        }