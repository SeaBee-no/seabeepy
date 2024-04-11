from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_ACCESS_ID: str
    MINIO_SECRET_KEY: str
    GEOSERVER_USER: str
    GEOSERVER_PASSWORD: str
    GEONODE_USER: str
    GEONODE_PASSWORD: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        case_sensitive = False
        env_file = ".env"


SETTINGS = Settings()
