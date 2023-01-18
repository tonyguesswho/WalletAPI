from apis.v1 import route_wallets
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_wallets.router, prefix="/wallet", tags=["wallet"])
