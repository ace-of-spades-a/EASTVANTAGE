import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Address Book.."
    BASE_URL: str = os.getenv("BASE_URL")
    DB_NAME: str = os.getenv("sqlite_db_name")
    JWT_SECRET: str = os.getenv("secret")
    JWT_ALGORITHM: str = os.getenv("algorithm")


settings = Settings()
