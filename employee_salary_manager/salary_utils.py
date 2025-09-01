# salary_utils.py

import json
from employee_module import Employee

EMPLOYEE_FILE = "employees.json"

def fetch_employees():
    """
    Simulates GET request by reading employees.json
    Returns a list of Employee objects
    """
    with open(EMPLOYEE_FILE, "r") as f:
        data = json.load(f)

    employees = []
    for emp in data["employees"]:
        employees.append(Employee(emp["id"], emp["name"], emp["salary"]))
    return employees


def post_salary_update(employee):
    """
    Simulates POST request by updating employees.json with new salary
    """
    with open(EMPLOYEE_FILE, "r") as f:
        data = json.load(f)

    for emp in data["employees"]:
        if emp["id"] == employee.emp_id:
            emp["salary"] = employee.salary

    with open(EMPLOYEE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return True
