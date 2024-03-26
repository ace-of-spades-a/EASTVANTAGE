from department import Department
from employee import Employee
import json


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print("Department already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print("Department does not exist.")

    def display_departments(self):
        print("Departments:")
        for department_name in self.departments:
            print(department_name)

    def save_company_data(self, filename):
        with open(filename, "w") as file:
            json.dump(
                self.departments,
                file,
                default=lambda obj: obj.__dict__,
                indent=4,
            )
        print("Company data saved successfully.")

    def load_company_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for department_name, employees_data in data.items():
                department = Department(department_name)
                for emp_data in employees_data:
                    employee = Employee(**emp_data)
                    department.add_employee(employee)
                self.departments[department_name] = department
        print("Company data loaded successfully.")
