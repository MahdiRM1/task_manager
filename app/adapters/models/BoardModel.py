from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.models.base import Base

class BoardModel(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('TaskModel', back_populates='board')