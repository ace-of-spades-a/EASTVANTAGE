class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return self.name
