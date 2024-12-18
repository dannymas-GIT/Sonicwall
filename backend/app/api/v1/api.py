from fastapi import APIRouter
from app.api.v1.endpoints import auth, security, log_analysis

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "SonicWall API"}

api_router.include_router(auth.router)
api_router.include_router(security.router)
api_router.include_router(log_analysis.router, prefix="/logs", tags=["log analysis"]) 