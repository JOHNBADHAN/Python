class Employee:
    name = "John"
    language = "Javascript"
    salary = 10000000

    def getInfo(self):
        print(f"The language is {self.language}")

    @staticmethod
    def greet():
        print("yoooo")

emp = Employee()
emp.getInfo()
emp.greet()