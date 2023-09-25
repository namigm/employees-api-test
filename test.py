# import os
#
# import pytest as pytest
# import requests
# from dotenv import load_dotenv
# from endpoints.employees import Employees
# from db.db_connection import DatabaseConnection
# from support.logger import save_log
#
# log = save_log()
#
#
# @pytest.fixture(scope="session", autouse=True)
# def db_connection():
#     connection = DatabaseConnection(
#         dbname="testbase",
#         user="postgres",
#         password="rooter",
#         host="localhost",
#         port="5432"
#     )
#     return connection
#
#
#
#
#
#
#
# def create_employees(db_connection):
#     created_users = []
#     cur = db_connection.connection.cursor()
#     cur.execute("SELECT MAX(employee_id) FROM employees")
#     max_employee_id = cur.fetchone()[0]
#     print(max_employee_id)
#     cur.close()
#
#
# create_employees()

test_1 = (5)
test_2 = (5,)
print(type(test_1))
print(type(test_2))
print(test_2[0])