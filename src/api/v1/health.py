from http import HTTPStatus

from fastapi import APIRouter, Response

from models.link import Link

router = APIRouter(
    prefix='/health',
    tags=['health'],
)


@router.get('')
async def check_health():
    status = HTTPStatus.OK

    try:
        await Link.all().count()
    except OSError:
        status = HTTPStatus.SERVICE_UNAVAILABLE

    return Response(status_code=status)
