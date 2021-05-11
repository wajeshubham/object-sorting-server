from fastapi import FastAPI, Request, status,WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc, desc
from app.api.routers import product
from app.api.base_response import BaseResponse
from app.core.config import settings
import random
from app.models.product import Product
from app.api.deps import get_db
import json
from datetime import datetime


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

def get_prods(db: Session=Depends(get_db)):
    product_list=db.query(Product).order_by(asc(Product.order)).all()
    return product_list

def get_prod_by_id(db:Session, id:str):
    product=db.query(Product).filter(Product.id == id).first()
    return product

def get_last_added_prod(db:Session):
    product=db.query(Product).order_by(desc(Product.updated_at)).all()
    return product[0]

@app.put("/product/{id}")
def increase_count( id:str,db:Session=Depends(get_db)):
    product=get_prod_by_id(db,id)
    product.count+=1
    product.updated_at=datetime.now()
    db.add(product)
    db.commit()
    db.refresh(product)
    LAST_ADDED_PRODUCT=jsonable_encoder(product)
    return {"prod":product}


@app.websocket("/ws")
async def send_data(websocket:WebSocket,db: Session = Depends(get_db)):
    print('CONNECTING...')
    await websocket.accept()
    count=[0,0,0,0,0,0,0,0,0]
   
    while True:
        try:
            ind=int(random.uniform(0,9))
            await websocket.receive_text()
            if ind==0:
                count[0]+=1
            if ind==1:
                count[1]+=1
            if ind==2:
                count[2]+=1
            if ind==3:
                count[3]+=1
            if ind==4:
                count[4]+=1
            if ind==5:
                count[5]+=1
            if ind==6:
                count[6]+=1
            if ind==7:
                count[7]+=1
            if ind==8:
                count[8]+=1

            prod=get_prods(db)
            last_added_product=get_last_added_prod(db)
            for i in range(len(prod)):
                db.refresh(prod[i])
            resp = {
            'value': jsonable_encoder(prod),
            "last_added":jsonable_encoder(last_added_product)
            }
            _resp = {'value': [
                    {
                        "type": 'T1',
                        "count":count[0],
                        "color": "red",
                        "shape":"circle",
                        "box_type":"box1"
                    },
                    {
                        "type": 'T2',
                        "count": count[1],
                        "color": "green",
                        "shape":"triangle",
                        "box_type":"box1"
                    },
                    {
                        "type": 'T3',                        
                        "count": count[2],
                        "color": "green",
                        "shape":"circle",
                        "box_type":"box1"
                    },
                    {
                        "type": 'T1',                        
                        "count": count[3],
                        "color": "blue",
                        "shape":"circle",
                        "box_type":"box2"
                    },
                    {
                        "type": 'T2',                        
                        "count": count[4],
                        "color": "green",
                        "shape":"square",
                        "box_type":"box2"
                    },
                    {
                        "type": 'T3',                        
                        "count": count[5],
                        "color": "blue",
                        "shape":"square",
                        "box_type":"box2"
                    },
                    {
                        "type": 'T1',                        
                        "count": count[6],
                        "color": "red",
                        "shape":"triangle",
                        "box_type":"box3"
                    },
                    {
                        "type": 'T2',                        
                        "count": count[7],
                        "color": "red",
                        "shape":"square",
                        "box_type":"box3"
                    },
                    {
                        "type": 'T3',                        
                        "count": count[8],
                        "color": "blue",
                        "shape":"triangle",
                        "box_type":"box3"
                    }
            ],
            "last_added":jsonable_encoder(last_added_product)
            }
            await websocket.send_json(resp)
        except Exception as e:
            print(e)
            break
    print("CONNECTION DEAD...")
