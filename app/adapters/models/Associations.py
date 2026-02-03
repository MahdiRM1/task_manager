from sqlalchemy import Table, Column, Integer, ForeignKey

from app.adapters.models.base import Base

task_tag = Table(
    'task_tag',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)
