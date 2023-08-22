from sqlalchemy import Column, Integer, String
from database import Base

# Table DB model definition
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

# Pydantic model definition
# Pydantic models are used to define the request and response models for the API endpoints.
# So DTO (Data Transfer Object)
