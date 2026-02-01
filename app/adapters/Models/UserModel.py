from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.Models.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    created_tasks = relationship('Task', back_populates='task_creator')
    assigned_tasks = relationship('Task', back_populates='task_assignee')
    notifs = relationship('Notification', back_populates='receiver')
    report_target = relationship('Report', foreign_keys='Report.target_user_id', back_populates='target_user')