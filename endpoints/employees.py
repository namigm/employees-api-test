import requests


class Employees:
    max_emp_id = 0

    def __init__(self, url: str, session: requests.Session, token: str):
        self.url = url
        self.session = session
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}',
                        'Content-Type': 'application/json'}

    def fetch_single_employee(self, employee_id, employee_data):
        response = self.session.get(url=f'{self.url}/{employee_id}', headers=self.headers)
        assert response.json() == employee_data, f"Actual data {response.json()}, but expected {employee_data}"
        assert response.status_code == 200, f"Actual status {response.status_code}, but expected 200"

    def add_employee(self, body, get_max_employee_id, get_employee_by_id):
        self.max_emp_id = get_max_employee_id
        created_emp_id = self.max_emp_id + 1
        add_employee = self.session.post(url=self.url, headers=self.headers, json=body)
        response = add_employee.json()
        assert response['employeeId'] == created_emp_id, f"response['employeeId'] is  {response['employeeId']}, but " \
                                                         f"expected {created_emp_id} "
        assert response['name'] == body['name'], f"response['name'] is  {response['name']}, but expected {body['name']}"
        assert response['organization'] == body[
            'organization'], f"response['organization'] is  " \
                             f"{response['organization']}, but expected {body['organization']} "
        assert response['role'] == body['role'], f"response['role'] is  {response['role']}, but expected {body['role']}"
        assert add_employee.status_code == 200
        """is added"""
        assert get_employee_by_id(created_emp_id)[0] == body['name']
        assert get_employee_by_id(created_emp_id)[1] == body['organization']
        assert get_employee_by_id(created_emp_id)[2] == body['role']

    def remove_emp_by_id(self, del_employee_by_id):
        return del_employee_by_id(self.max_emp_id + 1)

    def update_employee(self, body, first_created_employee_data):
        emp_id = first_created_employee_data["employeeId"]
        update_employee = self.session.put(url=f'{self.url}/{emp_id}', headers=self.headers, json=body)

        is_updated = self.session.get(url=f'{self.url}/{emp_id}', headers=self.headers)
        response = is_updated.json()
        assert update_employee.status_code == 200, f"Actual status_code is {update_employee.status_code} but expected " \
                                                   f"is 200 "
        assert update_employee.json() == {
            "message": "Employee updated"}, f"Actual message is  {update_employee.json()}, " \
                                            f"but expected message: Employee updated"
        """""""""""""""Is updated"""""""""""""""""
        assert is_updated.status_code == 200
        assert response["name"] == body["name"], f"response['name'] is  {response['name']}, but expected {body['name']}"
        assert response["organization"] == body["organization"], \
            f"response['organization'] is  {response['organization']}, " \
            f"but expected {body['organization']}"
        assert response["role"] == body["role"], f"response['role'] is  {response['role']}, " \
                                                 f"but expected {body['role']}"

    def part_update_employee(self, body, first_created_employee_data):
        emp_id = first_created_employee_data["employeeId"]
        update_employee = self.session.patch(url=f'{self.url}/{emp_id}', headers=self.headers, json=body)

        is_updated = self.session.get(url=f'{self.url}/{emp_id}', headers=self.headers)
        response = is_updated.json()
        assert update_employee.status_code == 200, f"Actual status_code is {update_employee.status_code} but expected " \
                                                   f"is 200 "
        assert update_employee.json() == {
            "message": "Employee updated"}, f"Actual message is  {update_employee.json()}, " \
                                            f"but expected message: Employee updated"
        """""""""""""""Is updated"""""""""""""""""
        assert is_updated.status_code == 200
        assert response["name"] == body["name"], f"response['name'] is  {response['name']}, but expected {body['name']}"
        assert response["organization"] == body["organization"], \
            f"response['organization'] is  {response['organization']}, " \
            f"but expected {body['organization']}"

    def delete_employee(self, first_created_employee_data):
        emp_id = first_created_employee_data["employeeId"]
        delete_employee = self.session.delete(url=f'{self.url}/{emp_id}', headers=self.headers)
        response = delete_employee.json()
        assert delete_employee.status_code == 200, f"Actual status_code is {delete_employee.status_code} but expected " \
                                            f"is 200 "
        assert response == {
            "message": "Employee deleted"}, f"Actual message is  {response}, " \
                                            f"but expected message: Employee deleted"

    def check_removed_employee(self, select_all_from_table):
        employees = [row[0] for row in select_all_from_table]
        assert "Namik" not in employees, f'Employee still in {employees}'


