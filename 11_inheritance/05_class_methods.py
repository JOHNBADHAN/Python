class Employee:
    a = 1

    # def show(self):
    #     print(f"The class attribute of a is {self.a}")

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

emp = Employee()
emp.a = 2

emp.show()