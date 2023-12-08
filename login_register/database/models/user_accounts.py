import sys
import os

sys.path.append(os.getcwd())

from sqlalchemy import Column, Integer, String
from database.config import Base

class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name = Column(String, nullable=False, index=True, )
    last_name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
