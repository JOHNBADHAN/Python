class Animal:
    pass

class Pets(Animal):
    pass

class dogs(Pets):

    @staticmethod
    def bark():
        print("bow! bow!")

a = dogs()
a.bark()