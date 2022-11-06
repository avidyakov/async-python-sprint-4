from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from starlette.responses import RedirectResponse

from src.models.link import Click, Link
from src.schemas.links import ClickModel, LinkInModel, LinkModel

router = APIRouter(
    prefix='/links',
    tags=['links'],
)


@router.post('', response_model=LinkModel)
async def create_link(link_data: LinkInModel):
    link = await Link.create(**link_data.dict())
    return await LinkModel.from_tortoise_orm(link)


@router.get('/{link_id}', response_class=RedirectResponse)
async def redirect(link_id: int):
    link = await Link.get(id=link_id)
    await Click.create(link=link)
    return link.origin


@router.get('/{link_id}/clicks', response_model=Page[ClickModel])
async def get_clicks(link_id: int):
    link = await Link.get(id=link_id)
    clicks = await ClickModel.from_queryset(link.clicks.all())
    return paginate(clicks)
