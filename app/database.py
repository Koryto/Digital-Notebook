from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgres://postgres:docker@localhost/dnotebook"

db = create_engine(SQLALCHEMY_DATABASE_URL)#, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)
session = SessionLocal()


