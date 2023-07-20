from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    JWT_ALGORITHM: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_URL: str
    DB_NAME: str
    DB_HOST: str

    class Config:
        env_file = ".env"


settings = Settings()
