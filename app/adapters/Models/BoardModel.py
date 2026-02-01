from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.Models.base import Base

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('Task', back_populates='board')