from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.adapters.Models.base import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    created_tasks = relationship('TaskModel', back_populates='task_creator')
    assigned_tasks = relationship('TaskModel', back_populates='task_assignee')
    notifs = relationship('NotificationModel', back_populates='receiver')
    created_reports = relationship('ReportModel', back_populates='creator')
    report_target = relationship('ReportModel', foreign_keys='ReportModel.target_user_id', back_populates='target_user')