class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(
            f"Name: {self.name}, ID: {self.emp_id}, Title: {self.title}, Department: {self.department}"
        )

    def __str__(self):
        return f"{self.name} ({self.emp_id})"
