from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.orm import relationship
from app.model import Base;

class Category(Base):
    __tablename__      = 'category'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    job                = Column(TEXT)
    listcleanerService = relationship("ListcleanerService", back_populates="category")

    def __init__(seft, job):
        seft.job = job
    
    def to_json(seft):
        return{
            'job' : seft.job
        }
