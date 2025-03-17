
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello my name is {self.name} and my age is {self.age} year"

person = Person("Abinash", 33)
print(person.greet())
