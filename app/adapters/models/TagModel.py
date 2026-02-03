from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.models.Associations import task_tag
from app.adapters.models.base import Base

class TagModel(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    tasks = relationship('TaskModel', secondary=task_tag, back_populates='tags')