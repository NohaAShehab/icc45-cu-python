
# class Employee:
#     pass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old.')

p = Person('John', 36)
print(isinstance(p, object))