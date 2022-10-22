from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src.db import host, user, password, port, database
from src.controller.AdminController import router as adminRouter

import aiomysql

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    title="API&DB Team Blog",
    version="1.0.0",
    middleware=middleware,
    root_path="/dev",
)

@app.on_event("startup")
async def _startup():
    app.state.pool = await aiomysql.create_pool(host=host, port=port, user=user, password=password, db=database)
    print("startup done")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.pool = app.state.pool
    response = await call_next(request)
    return response

@app.get(path="/", tags=["useless_intro"])
async def getIndex(request:Request):
  return "Bank API Resource"

app.include_router(adminRouter,prefix="/admin")


handler = Mangum(app)
