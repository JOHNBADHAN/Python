class Employee:
    company = "Microsoft"
    name = "John"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class language:
    language = "Python"
    def show2(self):
        print(f"The language of the Employee is {self.language}")

class Programmer(Employee,language):
    company = "Google"
    def show3(self):
        print(f"The name of company {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()


b.show()
b.show2()
b.show3()