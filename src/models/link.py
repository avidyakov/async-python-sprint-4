from urllib.parse import urljoin

from tortoise import Model, fields

from core.config import config
from models.base import BaseModel


class Link(Model):
    uid = fields.UUIDField(pk=True)
    origin = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    is_deleted = fields.BooleanField(default=False)

    def short(self) -> str:
        return urljoin(config.short_url_host, str(self.uid))

    class PydanticMeta:
        computed = ('short',)


class Click(BaseModel):
    created_at = fields.DatetimeField(auto_now_add=True)
    address = fields.CharField(max_length=255)

    link = fields.ForeignKeyField('models.Link', related_name='clicks')

    class PydanticMeta:
        excluded = ('link',)
