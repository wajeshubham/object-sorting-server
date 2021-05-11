from sqlalchemy import Column, Integer, String
from app.database.setup import Base
from .main_base_model import MainBaseModel


class Product(MainBaseModel, Base):
    __tablename__ = "product"

    id = Column(String, primary_key=True, index=True,nullable=False)
    color = Column(String, index=True, nullable=False)
    shape = Column(String, index=True, nullable=False)
    count = Column(Integer, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)
    box_type=Column(String, index=True, nullable=False)
    order=Column(Integer,index=True,nullable=True)


    
