from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.product import Product
from app.api.schemas.product import ProductPostObj
from app.api.deps import get_db

from services.product import get_prods, get_prod_by_id

router = APIRouter()

@router.post("/products")
def create_prods(data:List[ProductPostObj],db:Session=Depends(get_db)):
    for i in data:
        product=Product(**dict(i))
        db.add(product)
        db.commit()
        db.refresh(product)
    return {"res":"created successfully"}

@router.get("/products")
def get_all_prods(db:Session=Depends(get_db)):
    prods=get_prods(db)
    return prods

@router.put("/product/{id}")
def increase_count( id:str,db:Session=Depends(get_db)):
    product=get_prod_by_id(db,id)
    product.count+=1
    product.updated_at=datetime.now()
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"prod":product}