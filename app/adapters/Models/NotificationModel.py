from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.adapters.Models.base import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    receiver_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String)
    created_at = Column(DateTime)
    is_read = Column(Boolean)

    receiver = relationship('User', back_populates='notifs')