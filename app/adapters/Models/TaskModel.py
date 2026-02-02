from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.adapters.Models.Associations import task_tag
from app.adapters.Models.base import Base

class TaskModel(Base):
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

    task_creator = relationship('UserModel', foreign_keys=[creator_id], back_populates='created_tasks')
    task_assignee = relationship('UserModel', foreign_keys=[assignee_id], back_populates='assigned_tasks')
    board = relationship('BoardModel', back_populates='tasks')
    report_target = relationship('ReportModel', foreign_keys='ReportModel.target_task_id', back_populates='target_task')
    tags = relationship('TagModel', secondary=task_tag, back_populates='tasks')