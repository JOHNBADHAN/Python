class Employee:
    name = "John"
    language = "Javascript"  # This is a class attribute
    salary = 10000000

emp = Employee()
emp.age = 21 # This is an instance attribute
print(emp.name, emp.salary, emp.age)