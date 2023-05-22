import secrets
from typing import Any, Dict, List, Optional, Union
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
import os
import sys

class Settings(BaseSettings):
    API_V1_STR: str = os.getenv("API_V1_STR")
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    pyversion = '{0[0]}.{0[1]}'.format(sys.version_info)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv(os.path.join(dir_path, '.env'))

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
       os.getenv("ORIGINAL_HOST"),
       os.getenv("HTTPCORSLOCALHOST"),
       os.getenv("LOCALHOSTDEVCORS")
    ]

    PROJECT_NAME: str = os.getenv("PROJECTNAME")

class Config:
    case_sensitive = True


settings = Settings()
