from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.orm import relationship
from app.model import Base;

class Role(Base):
    __tablename__ = 'role'
    id            = Column(Integer, primary_key=True, autoincrement=True)
    name          = Column(TEXT)
    account       = relationship("Account", back_populates="role")

    def __init__(seft, name):
        seft.name = name
    
    def to_json(seft):
        return{
            'name' : seft.name
        }