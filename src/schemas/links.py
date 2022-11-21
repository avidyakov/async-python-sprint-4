from tortoise.contrib.pydantic import pydantic_model_creator

from models.link import Click, Link

LinkModel = pydantic_model_creator(Link, name='Link')
LinkInModel = pydantic_model_creator(
    Link,
    name='LinkIn',
    exclude=('uid', 'is_deleted', 'created_at'),
    exclude_readonly=True,
)

ClickModel = pydantic_model_creator(Click, name='Click')
