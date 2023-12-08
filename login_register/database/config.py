from dotenv import load_dotenv
import os

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = f'postgresql://{os.getenv("USERNAME_DB")}:{os.getenv("PASSWORD_DB")}@postgres:5432/UserAccounts'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()