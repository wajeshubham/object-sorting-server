from fastapi import APIRouter,WebSocket, Depends, status, Request
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.api.deps import get_db

router = APIRouter()

# @router.websocket("/ws")
# # @router.get("/data")
# async def send_data(websocket:WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             await websocket.receive_text()
#             data=[
#                     {
#                         "name": "Page A",
#                         "uv": 4000,
#                         "pv": 2400,
#                         "amt": 2400,
#                     },
#                     {
#                         "name": "Page B",
#                         "uv": 3000,
#                         "pv": 1398,
#                         "amt": 2210,
#                     },
#                     {
#                         "name": "Page C",
#                         "uv": 2000,
#                         "pv": 9800,
#                         "amt": 2290,
#                     },
#                     {
#                         "name": "Page D",
#                         "uv": 2780,
#                         "pv": 3908,
#                         "amt": 2000,
#                     },
#                     {
#                         "name": "Page E",
#                         "uv": 1890,
#                         "pv": 4800,
#                         "amt": 2181,
#                     },
#                     {
#                         "name": "Page F",
#                         "uv": 2390,
#                         "pv": 3800,
#                         "amt": 2500,
#                     },
#                     {
#                         "name": "Page G",
#                         "uv": 3490,
#                         "pv": 4300,
#                         "amt": 2100,
#                     },
#                 ]
#             await websocket.send_json(data)
#         except Exception as e:
#             print(e)
#             break
#     print("Bye...")