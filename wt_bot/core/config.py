from typing import Optional, Dict, Any

from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, validator

class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_TEST_DB: str
    POSTGRES_DB: str
    POSTGRES_PORT: int


    FIRST_SUPERUSER_PASSWORD:str
    FIRST_SUPERUSER :str

    ALGORITHM:str
    SECRET_KEY:str

    SQLALCHEMY_TEST_DATABASE_URI: Optional[PostgresDsn] = None


    OPENAI_ENGINE :str
    OPENAI_API_VERSION : str
    OPENAI_API_KEY : str
    OPENAI_API_BASE : str
    TEMPERATURE : str


    E_ENGINE :str
    E_OPENAI_API_VERSION : str
    E_OPENAI_API_KEY : str
    E_OPENAI_API_BASE : str
    #E_OPENAI_API_TYPE:str


    @validator("SQLALCHEMY_TEST_DATABASE_URI", pre=True)
    def assemble_test_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_TEST_DB') or ''}",
            port=values.get('POSTGRES_PORT')
        )


    ACCESS_TOKEN_EXPIRE_MINUTES:int
    class Config:
            env_file = ".env"


settings = Settings()
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
print("printing...")
print(SQLALCHEMY_DATABASE_URL)
print("done...")
