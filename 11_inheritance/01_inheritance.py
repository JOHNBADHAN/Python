class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "vvhj"
    def emp(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

a = Employee()
b = Programmer()

print(a.company, b.company)