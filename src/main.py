import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api import router
from src.core.config import config

app = FastAPI(
    title=config.project_name,
    default_response_class=ORJSONResponse,
)

app.include_router(router.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=config.host, port=config.port)
