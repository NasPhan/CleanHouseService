from sqlalchemy import Column, Integer, TEXT, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Base;
from app.model.category import Category

class ListcleanerService(Base):
    __tablename__ = 'listcleanerService'
    id            = Column(Integer, primary_key=True,autoincrement=True)
    accountId     = Column(ForeignKey("user.id"))
    categoryId    = Column(ForeignKey("user.id"))
    user          = relationship("Users", back_populates="listcleanerService")

    def __init__(seft, accountId, categoryId):
        seft.accountId   = accountId 
        seft.categoryId  = categoryId
    
    def to_json(seft):
        return {
            'accountId'  : Category.to_json(seft.accountId),
            'categoryId' : Category.to_json(seft.categoryId),
        }
