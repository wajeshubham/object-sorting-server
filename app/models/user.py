from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import relationship, validates
import re
from app.database.setup import Base
from .main_base_model import MainBaseModel


class User(MainBaseModel, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    
