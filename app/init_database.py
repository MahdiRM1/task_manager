from sqlalchemy import create_engine
from app.adapters.models.base import Base

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)