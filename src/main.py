import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_pagination import add_pagination

from src.api import router
from src.core.config import config
from src.db import register_db

app = FastAPI(
    title=config.project_name,
    default_response_class=ORJSONResponse,
)

app.include_router(router.router)

register_db(app)
add_pagination(app)

if __name__ == '__main__':
    uvicorn.run('main:app', host=config.host, port=config.port)
