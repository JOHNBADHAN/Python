class Programmer:
    company = "microsoft"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Programmer("John", 987655678)
print(emp.name, emp.salary)
emp = Programmer("Sam", 98765434)
print(emp.name, emp.salary)