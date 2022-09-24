from app.api.v1.endpoints import get_data
from fastapi import APIRouter

v1_router = APIRouter()
v1_router.include_router(
    get_data.router,
    prefix="/v1",
)
