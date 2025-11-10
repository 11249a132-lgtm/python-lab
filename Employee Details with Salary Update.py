Aim:
To write a Python program that creates a class Employee to store Name, Employee_ID, Department, and Salary, and implements a method to update the salary of employees belonging to a given department.

Algorithm:
Start the program.
Define a class Employee with attributes: name, employee_id, department, and salary.
Implement a method update_salary(department, increment) that:
Checks if the employee belongs to the given department.
Updates the salary by the given increment.
Create a list to store multiple Employee objects.
Input employee details from the user.
Display the employee details before salary update.
Input the department and increment amount for salary update.
Call the update_salary() method for all employees.
Display the employee details after salary update.
End the program.
Program (Python Code):
# Program: Employee Details with Salary Update
class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    # Method to update salary for a given department
    def update_salary(self, department, increment):
        if self.department.lower() == department.lower():
            self.salary += increment
    # Method to display employee details
    def display(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, "
              f"Department: {self.department}, Salary: {self.salary}")

# Main Program
employees = []
# Input number of employees
n = int(input("Enter number of employees: "))
# Input employee details
for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))
    employees.append(Employee(name, emp_id, dept, salary))
# Display employee details before salary update
print("\n=== Employee Details Before Salary Update ===")
for emp in employees:
    emp.display()
# Input department and increment for salary update
dept_update = input("\nEnter department for salary update: ")
increment = float(input("Enter salary increment: "))
# Update salary
for emp in employees:
    emp.update_salary(dept_update, increment)
# Display employee details after salary update
print("\n=== Employee Details After Salary Update ===")
for emp in employees:
    emp.display()
Result:

The program successfully:
Stores employee details in a class.
Displays employee information.
Updates salaries of employees belonging to a specific department.

This demonstrates object-oriented programming concepts like class, method, and encapsulation.
