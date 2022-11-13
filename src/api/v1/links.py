from http import HTTPStatus

from fastapi import APIRouter, Request
from fastapi_pagination import Page, paginate
from starlette.responses import RedirectResponse, Response

from src.models.link import Click, Link
from src.schemas.links import ClickModel, LinkInModel, LinkModel

router = APIRouter(
    prefix='/links',
    tags=['links'],
)


@router.post('', response_model=LinkModel | list[LinkModel])
async def create_link(links_data: LinkInModel | list[LinkInModel]):
    if isinstance(links_data, LinkInModel):
        links_data = [links_data]

    created = [await Link.create(**data.dict()) for data in links_data]
    return [await LinkModel.from_tortoise_orm(link) for link in created]


@router.get('/{link_id}', response_class=RedirectResponse)
async def redirect(link_id: int, request: Request):
    link = await Link.get(id=link_id, is_deleted=False)
    await Click.create(link=link, address=':'.join(map(str, request.client)))
    return link.origin


@router.delete('/{link_id}')
async def delete_link(link_id: int):
    link = await Link.get(id=link_id, is_deleted=False)
    link.is_deleted = True
    await link.save()
    return Response(status_code=HTTPStatus.NO_CONTENT)


@router.get('/{link_id}/clicks', response_model=Page[ClickModel])
async def get_clicks(link_id: int):
    link = await Link.get(id=link_id, is_deleted=False)
    clicks = await ClickModel.from_queryset(link.clicks.all())
    return paginate(clicks)
