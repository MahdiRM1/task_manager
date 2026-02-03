from sqlalchemy.orm import sessionmaker

from app.adapters.engine import engine

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
