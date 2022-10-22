import aiomysql
from src.DTO.User import User

async def getUser(pool,username:str):
    query = f"SELECT * FROM ADMIN WHERE username = '{username}';"
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            await conn.commit()
            return await cur.fetchone()

async def saveUser(pool,user:User):
    query = f"INSERT INTO ADMIN (username, password, role) VALUES ('{user.username}','{user.password}','{user.role}');"
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            await conn.commit()
            
