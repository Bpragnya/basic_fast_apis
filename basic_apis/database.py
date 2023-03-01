from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

#SQLALCHEMY_DATABASE_URL = "sqlite:///./basic_apis.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
#"postgresql://postgres:root@localhost:5432/basic_apis"
#postgresql://basic_api_db_user:MGPF89SPqa6a3QkJ1zI43FC3OSuPJmkZ@dpg-cfveemfdvk4rro5f356g-a.singapore-postgres.render.com/basic_api_db


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    #, connect_args={"check_same_thread": False #only for sql}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()