from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_class import Base

def create_tables(settings):
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
    print("Database URL is ", SQLALCHEMY_DATABASE_URL)
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)