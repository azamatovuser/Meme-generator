from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL_DATABASE = "sqlite:///./memes.db"

engine = create_engine(SQLALCHEMY_URL_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)