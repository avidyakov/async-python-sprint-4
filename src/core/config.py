from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    project_name: str
    host: str
    port: int
    database_dsn: PostgresDsn
    short_url_host: str

    class Config:
        env_file = '.env', '.env.template'


config = Config()
