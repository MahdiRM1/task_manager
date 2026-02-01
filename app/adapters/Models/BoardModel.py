from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('Task', back_populates='board')