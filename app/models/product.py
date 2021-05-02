from sqlalchemy import Column, Integer, String
from app.database.setup import Base
from .main_base_model import MainBaseModel


class Product(MainBaseModel, Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, index=True, nullable=False)
    shape = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)


    
