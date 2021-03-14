from sqlalchemy import Column, DateTime
import datetime


class MainBaseModel():
    created_at = Column(DateTime, index=True,default = datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, index=True, default= datetime.datetime.now, nullable=False)
    deleted_at = Column(DateTime, index=True)
