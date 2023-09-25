import pytest


def test_get_single_employees(employees_endpoint, get_id_created_employees, first_created_employee_data):
    employees_endpoint.fetch_single_employee(employee_id=get_id_created_employees,
                                             employee_data=first_created_employee_data)


@pytest.mark.parametrize('body,response_body', [({
                                                     "name": "Togrul",
                                                     "organization": "Business",
                                                     "role": "AQA"
                                                 }, {
                                                     "employeeId": 4,
                                                     "name": "Togrul",
                                                     "organization": "Business",
                                                     "role": "AQA"
                                                 })])
def test_add_employee(employees_endpoint, body, response_body, get_max_employee_id,
                      get_employee_by_id, del_employee_by_id):
    employees_endpoint.add_employee(body=body,
                                    get_max_employee_id=get_max_employee_id,
                                    get_employee_by_id=get_employee_by_id)
    employees_endpoint.remove_emp_by_id(del_employee_by_id)

def test_update_employee(employees_endpoint, first_created_employee_data):
    employees_endpoint.update_employee(first_created_employee_data=first_created_employee_data, body={
        "name": "Jamal",
        "organization": "Kinder Garden",
        "role": "Member"
    })


def test_part_update_employee(employees_endpoint, first_created_employee_data):
    employees_endpoint.part_update_employee(first_created_employee_data=first_created_employee_data, body={
        "name": "Namik",
        "organization": "GLO"
    })

def test_delete_employee(employees_endpoint, first_created_employee_data, select_all_from_table):
    employees_endpoint.delete_employee(first_created_employee_data=first_created_employee_data)
    employees_endpoint.check_removed_employee(select_all_from_table=select_all_from_table)
