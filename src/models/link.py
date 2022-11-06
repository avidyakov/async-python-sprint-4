from tortoise import fields
from tortoise.models import Model


class Link(Model):
    id = fields.IntField(pk=True)
    origin = fields.CharField(max_length=255)
    codename = fields.CharField(max_length=255)
    create_date = fields.DatetimeField(autho_now=True)
    clicks = fields.IntField(default=0)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}'
            f'({self.id}, {self.origin}, '
            f'{self.codename}, {self.create_date})'
        )
