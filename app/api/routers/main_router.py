from fastapi import APIRouter
from app.api.routers.user import user_router

router = APIRouter()

@router.get('/')
async def home_page():
    return {"msg": "API is working fine"}

router.include_router(user_router)


