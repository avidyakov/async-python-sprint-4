from fastapi import APIRouter

router = APIRouter(
    prefix='/links',
    tags=['links'],
)


@router.post('')
async def create_link():
    return {'version': 'v1'}
