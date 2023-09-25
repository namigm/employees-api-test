import os

import time
import pytest as pytest
import requests
from dotenv import load_dotenv
from endpoints.employees import Employees
from db.db_connection import DatabaseConnection
from support.logger import save_log
import json

log = save_log()


# ***********************Database fixtures************************

@pytest.fixture(scope="session", autouse=True)
def db_connection():
    connection = DatabaseConnection(
        dbname="testbase",
        user="postgres",
        password="rootroot",
        host="localhost",
        port="5432"
    )
    log.info(f"Connection to DB using creds: {connection.connection}")

    yield connection

    log.info(f"Close DB connection")
    connection.close()


@pytest.fixture(scope="session", autouse=True)
def create_employees(db_connection):
    created_users = []
    cur = db_connection.connection.cursor()
    cur.execute("SELECT MAX(employee_id) FROM employees")
    max_employee_id = cur.fetchone()[0]
    cur.close()

    user_data_list = [
        {"name": "Eddy", "organization": "IT", "role": "Lead Developer"},
        {"name": "Jack", "organization": "Finance", "role": "Accountant"},
        {"name": "Ariel", "organization": "Marketing", "role": "Marketing Specialist"}
    ]

    for user_data in user_data_list:
        max_employee_id = max_employee_id + 1 if max_employee_id is not None and max_employee_id != 0 else 1
        user_id = db_connection.fetchone(
            "INSERT INTO employees (employee_id, name, organization, role) VALUES (%s, %s, %s, %s) RETURNING employee_id",
            max_employee_id, user_data["name"], user_data["organization"], user_data["role"]
        )[0]

        user_info = {
            "employeeId": user_id,
            "name": user_data["name"],
            "organization": user_data["organization"],
            "role": user_data["role"]
        }

        created_users.append(user_info)
        db_connection.connection.commit()

    if created_users:
        with open("first_created_employee.json", "w") as json_file:
            json.dump(created_users[0], json_file)

    log.info(f"Test data set has been created: {created_users}")

    return created_users


@pytest.fixture(scope="session", autouse=True)
def delete_employees(db_connection, create_employees):
    yield
    time.sleep(15)
    for user in create_employees:
        user_id = user.get("employeeId")
        log.info(f"Test data set has been deleted: {user_id}")
        db_connection.execute("DELETE FROM employees WHERE employee_id = %s", user_id)


@pytest.fixture(scope="function")
def get_id_created_employees(create_employees):
    employee_id = next((user["employeeId"] for user in create_employees if user["name"] == "Eddy"), None)
    log.info(f"Getting required ID: {employee_id}")
    return employee_id


@pytest.fixture(scope="session")
def first_created_employee_data():
    with open("first_created_employee.json", "r") as json_file:
        data = json.load(json_file)
    log.info(f"Getting required data: {data}")
    return data


@pytest.fixture()
def get_max_employee_id(db_connection):
    cur = db_connection.connection.cursor()
    cur.execute("SELECT MAX(employee_id) FROM employees")
    max_employee_id = cur.fetchone()[0]
    cur.close()
    return max_employee_id


@pytest.fixture()
def get_employee_by_id(db_connection):
    def get_emp(emp_id):
        cur = db_connection.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE employee_id = %s", (emp_id,))
        employee = cur.fetchone()
        cur.close()
        return employee

    return get_emp


@pytest.fixture()
def del_employee_by_id(db_connection):
    def del_emp(emp_id):
        cur = db_connection.connection.cursor()
        cur.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
        db_connection.connection.commit()
        cur.close()
    return del_emp


@pytest.fixture()
def select_all_from_table(db_connection):
    cur = db_connection.connection.cursor()
    cur.execute("SELECT * from employees")
    data = cur.fetchall()
    cur.close()
    return data


# ***********************App fixtures************************


load_dotenv()


@pytest.fixture()
def create_session():
    yield requests.Session()


@pytest.fixture()
def token():
    def get_auth_token():
        credentials = {
            "username": os.getenv('APP_SUPERUSER'),
            "password": os.getenv('APP_PASSWORD')}
        token_request = requests.post(f'{os.getenv("TOKEN_URL")}', json=credentials)
        return token_request

    def validate_token(token_request):
        if token_request.status_code == 401:
            raise ValueError('Unauthorized: Invalid credentials')
        elif 'token' not in token_request.text:
            raise EnvironmentError("Token not found in the response")
        return token_request

    return validate_token(get_auth_token()).json()['token']


@pytest.fixture()
def employees_endpoint(create_session, token):
    return Employees(session=create_session, token=token, url=os.getenv("EMPLOYEES_URL"))
