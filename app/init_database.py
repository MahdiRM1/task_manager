from app.adapters.models.base import Base
from app.adapters.engine import engine

Base.metadata.create_all(bind=engine)