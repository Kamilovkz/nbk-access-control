from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_KEY: str
    TEST_VARIABLE: str

    class Config:
        env_file = ".env"


settings = Settings()
