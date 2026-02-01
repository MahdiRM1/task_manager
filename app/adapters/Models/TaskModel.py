from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id'))
    assignee_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    board_id = Column(Integer, ForeignKey('boards.id'))
    deadline = Column(DateTime)
    created_at = Column(DateTime)
    status = Column(String)

    task_creator = relationship('User', foreign_keys=[creator_id], back_populates='created_tasks')
    task_assignee = relationship('User', foreign_keys=[assignee_id], back_populates='assigned_tasks')
    board = relationship('Board', back_populates='tasks')
    report_target = relationship('Report', foreign_keys='Report.target_task_id', back_populates='target_task')
    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')