from typing import Optional
from pydantic.main import BaseModel
from datetime import datetime

class ProductPostObj(BaseModel):
    deleted_at:Optional[datetime]=None
    created_at: datetime
    color: str
    shape: str
    type: str
    order: int
    updated_at: datetime
    id: str
    count:int
    box_type: str