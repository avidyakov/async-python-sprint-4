from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    project_name: str = 'linkvid'
    host: str = '0.0.0.0'
    port: int = 8000
    database_dsn: PostgresDsn = (
        'postgres://admin:admin@localhost:5432/postgres'
    )
    short_url_host: str = 'http://localhost:8000/v1/links/'

    class Config:
        env_file = '.env'


config = Config()
