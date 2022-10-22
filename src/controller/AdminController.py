from fastapi import APIRouter, Request
from src.DTO.User import User
from src.DTO.Login import Login
from src.service import AdminService

router = APIRouter()

@router.post("/login")
async def getUser(request:Request, login:Login):
    return await AdminService.getUser(request.state.pool,login)

@router.post("/save")
async def saveUser(request:Request, user:User):
    return await AdminService.saveUser(request.state.pool,user)
