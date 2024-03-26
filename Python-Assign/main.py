import json
from company import Company
from employee import Employee


def print_menu():
    print("\nMenu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. List Departments")
    print("4. Add Employee to Department")
    print("5. Remove Employee from Department")
    print("6. List Employees in Department")
    print("7. Save Company Data")
    print("8. Load Company Data")
    print("9. Exit")


def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            department_name = input("Enter department name: ")
            company.add_department(department_name)
        elif choice == "2":
            department_name = input("Enter department name: ")
            company.remove_department(department_name)
        elif choice == "3":
            company.display_departments()
        elif choice == "4":
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                employee = Employee(name, emp_id, title, department_name)
                company.departments[department_name].add_employee(employee)
                print("Employee added successfully.")
            else:
                print("Department does not exist.")
        elif choice == "5":
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                employee_id = input("Enter employee ID to remove: ")
                for employee in company.departments[department_name].employees:
                    if employee.emp_id == employee_id:
                        company.departments[department_name].remove_employee(
                            employee
                        )
                        print("Employee removed successfully.")
                        break
                else:
                    print("Employee not found.")
            else:
                print("Department does not exist.")
        elif choice == "6":
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Department does not exist.")
        elif choice == "7":
            filename = input("Enter filename to save company data: ")
            company.save_company_data(filename)
        elif choice == "8":
            filename = input("Enter filename to load company data: ")
            company.load_company_data(filename)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
