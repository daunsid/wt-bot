from fastapi import APIRouter

from wt_bot.api.v1.endpoints import users, utils, ws

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
#api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(ws.router, prefix="/apgar", tags=["chat"])
