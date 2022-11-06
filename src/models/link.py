from urllib.parse import urljoin

from tortoise import fields

from src.core.config import config
from src.models.base import BaseModel


class Link(BaseModel):
    origin = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    def short(self) -> str:
        return urljoin(config.short_url_host, str(self.id))

    class PydanticMeta:
        computed = ('short',)


class Click(BaseModel):
    created_at = fields.DatetimeField(auto_now=True)
    link = fields.ForeignKeyField('models.Link', related_name='clicks')

    class PydanticMeta:
        excluded = ('link',)
