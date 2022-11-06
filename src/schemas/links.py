from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.link import Click, Link

LinkModel = pydantic_model_creator(Link, name='Link')
LinkInModel = pydantic_model_creator(
    Link, name='LinkIn', exclude_readonly=True
)

ClickModel = pydantic_model_creator(Click, name='Click')
