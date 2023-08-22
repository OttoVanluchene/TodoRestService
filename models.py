from sqlalchemy import Column, Integer, String
from database import Base

# Table DB model definition
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
