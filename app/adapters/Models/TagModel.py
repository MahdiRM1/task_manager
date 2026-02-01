from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.Models.Associations import task_tag
from app.adapters.Models.base import Base

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('Task', secondary=task_tag, back_populates='tags')