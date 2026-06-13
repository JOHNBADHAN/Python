class Employee:
    name = "John"
    language = "Javascript"
    salary = 10000000

    def __init__(self, name, salary): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        print("Crazy")

    def getInfo(self):
        print(f"The language is {self.language}")

    @staticmethod
    def greet():
        print("yoooo")

emp = Employee("Sam", 1234567)
print(emp.name, emp.salary)
# emp.getInfo()
# emp.greet()   