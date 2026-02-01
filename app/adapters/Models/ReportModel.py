from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.adapters.Models.base import Base

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    target_user_id = Column(Integer, ForeignKey('users.id'))
    target_task_id = Column(Integer, ForeignKey('tasks.id'))
    created_at = Column(DateTime)

    target_user = relationship('User', foreign_keys=[target_user_id], back_populates='report_target')
    target_task = relationship('Task', foreign_keys=[target_task_id], back_populates='report_target')