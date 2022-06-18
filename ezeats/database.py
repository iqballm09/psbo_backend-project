from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

## Koleksi Favorit
SQLALCHEMY_DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False, 'timeout': 15})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Define get DB
def get_db() -> Session:
    db = SessionLocal()
    return db