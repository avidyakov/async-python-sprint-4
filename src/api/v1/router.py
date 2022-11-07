from fastapi import APIRouter

from src.api.v1 import health, links

router = APIRouter(prefix='/v1')
router.include_router(links.router)
router.include_router(health.router)
