from fastapi import APIRouter

from src.api.v1 import links

router = APIRouter(prefix='/v1')
router.include_router(links.router)
