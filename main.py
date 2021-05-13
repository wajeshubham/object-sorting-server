from app.models.product import Product
from app.api.schemas.product import ProductPostObj
from typing import List
from fastapi import FastAPI, WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

from sqlalchemy.orm import Session

from app.core.config import settings
from app.api.deps import get_db
from app.api.routers import product

from datetime import datetime

from services.product import get_prods, get_last_added_prod, get_prod_by_id

app = FastAPI(
    title=settings.APP_NAME,
    description="Inventory server",
    version="0.0.1",
)

origins = settings.CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/products")
def create_prods(data:List[ProductPostObj],db:Session=Depends(get_db)):
    for i in data:
        product=Product(**dict(i))
        db.add(product)
        db.commit()
        db.refresh(product)
    return {"res":"created successfully"}

@app.get("/products")
def get_all_prods(db:Session=Depends(get_db)):
    prods=get_prods(db)
    return prods

@app.post("/product/{id}")
def increase_count( id:str,db:Session=Depends(get_db)):
    product=get_prod_by_id(db,id)
    product.count+=1
    product.updated_at=datetime.now()
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"prod":product}

@app.post("/products/reset-count")
def reset_count(db:Session=Depends(get_db)):
    products=get_prods(db)
    for product in products:
        product.count=0
        product.updated_at=datetime.now()
        db.add(product)
        db.commit()
        db.refresh(product)
    return {"res":"count reset successful"}


@app.websocket("/ws")
async def send_data(websocket:WebSocket, db: Session = Depends(get_db)):
    print('CONNECTING...')
    await websocket.accept()
    while True:
        try:
            await websocket.receive_text()
            prod=get_prods(db)
            last_added_product=get_last_added_prod(db)

            for i in range(len(prod)):
                db.refresh(prod[i])

            resp = {
            'value': jsonable_encoder(prod),
            "last_added":jsonable_encoder(last_added_product)
            }
            await websocket.send_json(resp)
        except Exception as e:
            print(e)
            break
    print("CONNECTION DEAD...")

# app.include_router(product.router)
