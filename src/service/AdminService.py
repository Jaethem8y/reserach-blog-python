from passlib.context import CryptContext

from src.repository import AdminRepository
from src.DTO.Login import Login
from src.DTO.User import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def getUser(pool,login:Login):
    dbUser = await AdminRepository.getUser(pool,login.username)
    print(f"\n\n\n\n\n\n\n{dbUser}\n\n\n\n\n\n")
    if not dbUser:
        return False
    if not pwd_context.verify(login.password, dbUser["password"]):
        return False
    return True

async def saveUser(pool,user:User):
    user.password = pwd_context.hash(user.password)
    try:
        return await AdminRepository.saveUser(pool,user)
    except Exception as e:
        raise Exception("Save Failed")
