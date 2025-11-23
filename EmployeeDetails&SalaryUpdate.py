class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, "
              f"Department: {self.department}, Salary: {self.salary}")


def update_salary(employees, department, increment):
    """Update salary of employees in the given department."""
    for emp in employees:
        if emp.department == department:
            emp.salary += increment


# ---- Main Program ----
# Creating employee objects
e1 = Employee("Alice", 101, "HR", 40000)
e2 = Employee("Bob", 102, "IT", 55000)
e3 = Employee("Charlie", 103, "IT", 60000)

# List of employees
emp_list = [e1, e2, e3]

print("Before Update:")
for emp in emp_list:
    emp.display()

# Update salary of IT department employees
update_salary(emp_list, "IT", 5000)

print("\nAfter Update:")
for emp in emp_list:
    emp.display()
