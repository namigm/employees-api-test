import requests


# employee_table_url = "http://localhost:5000/employees"
# credentials = {
#     "username": "admin",
#     "password": "admin"
# }

# response = requests.post('http://localhost:5000/generate-token', json=credentials)
# token = response.json()['token']


def add_employee(token):
    headers = {"Authorization": f"Bearer {token}"}
    add_employee_body = {
        "name": "Togrul",
        "organization": "Business",
        "role": "AQA"
    }
    add_employee = requests.post(url=employee_table_url, headers=headers, json=add_employee_body)






check_employee_table = requests.get(url=employee_table_url, headers=headers)
print(check_employee_table.json())

delete_employee_url = 'http://localhost:5000//employees/1'

delete_employee = requests.delete(url=delete_employee_url, headers=headers)

print(requests.get(url=employee_table_url, headers=headers).json(), "employee removed")

part_update_emp_url = 'http://localhost:5000//employees/1'
part_update_emp_body = {
    "role": "Senior DevOps"
}
requests.post(url=employee_table_url, headers=headers, json=add_employee_body)

requests.patch(url=part_update_emp_url, headers=headers, json=part_update_emp_body)

print(requests.get(url=employee_table_url, headers=headers).json(), "role is updated")

update_emp_url = 'http://localhost:5000//employees/1'

update_emp_body = {
    "name": "Jenny",
    "organization": "IT",
    "role": "DevOps"
}

requests.patch(url=update_emp_url, headers=headers, json=update_emp_body)

print(requests.get(url=employee_table_url, headers=headers).json(), "employee updated")

print(requests.get(url=f'{employee_table_url}/1', headers=headers).json(), "check exist employee")
print(requests.get(url=f'{employee_table_url}/2', headers=headers).json(), "check not exist employee")
