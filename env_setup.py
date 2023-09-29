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


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SINGLE_EMP_SCHEMA = os.path.join(ROOT_PATH, 'schemas', 'single_employee_schema.json')
ADD_EMP_SCHEMA = os.path.join(ROOT_PATH, "schemas", 'add_employee_schema.json')
ALL_EMP_SCHEMA = os.path.join(ROOT_PATH, 'schemas', 'all_employee_schema.json')
UPDATE_EMP_SCHEMA = os.path.join(ROOT_PATH, 'schemas', 'update_employee_schema.json')
PART_UPDATE_EMP_SCHEMA = os.path.join(ROOT_PATH, 'schemas', 'part_update_employee_schema.json')
DEL_EMP_SCHEMA = os.path.join(ROOT_PATH, 'schemas', 'delete_employee_schema.json')

