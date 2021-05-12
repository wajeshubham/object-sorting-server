from fastapi.params import Depends

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc, desc

from app.models.product import Product
from app.api.deps import get_db

def get_prods(db: Session=Depends(get_db)):
    product_list=db.query(Product).order_by(asc(Product.order)).all()
    return product_list

def get_prod_by_id(db:Session, id:str):
    product=db.query(Product).filter(Product.id == id).first()
    return product

def get_last_added_prod(db:Session):
    product=db.query(Product).order_by(desc(Product.updated_at)).all()
    return product[0]