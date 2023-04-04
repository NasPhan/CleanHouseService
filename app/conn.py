from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:1111@localhost:8080/cleanhouse-test")
Session = sessionmaker(bind=engine)

