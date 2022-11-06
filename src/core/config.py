from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    project_name: str = 'linkvid'
    host: str = '0.0.0.0'
    port: int = 8000
    database_dsn: PostgresDsn = (
        'postgresql+asyncpg://admin:admin@localhost:5432/postgres'
    )

    class Config:
        env_file = '.env'


config = Config()
