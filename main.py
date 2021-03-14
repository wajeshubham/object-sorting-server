from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.base_response import BaseResponse
from app.api.routers import users
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="FastAPI production ready authentication system",
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

# this function will validate all the request parameters (kind of a middleware)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    res = []
    for error_obj in exc.errors():
        res.append({error_obj['loc'][-1]: error_obj['msg']})
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=BaseResponse.error_response(error=res, status=status.HTTP_400_BAD_REQUEST)
    )
