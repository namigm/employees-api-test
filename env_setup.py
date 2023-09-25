import os
from dotenv import load_dotenv
from dataclasses import dataclass

CONNECTION_STRING_DB = os.getenv("CONNECTION_STRING_DB")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


@dataclass
class Credentials:
    load_dotenv()
    APP_SUPERUSER: str = os.getenv("APP_SUPERUSER")
    APP_PASSWORD: str = os.getenv("APP_PASSWORD")

    @classmethod
    def get_env_variables(cls):
        if not Credentials.APP_SUPERUSER or not Credentials.APP_PASSWORD:
            raise "Error"
        return cls(Credentials.APP_SUPERUSER, Credentials.APP_PASSWORD)


print(Credentials.get_env_variables())

