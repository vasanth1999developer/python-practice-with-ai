

class Animal:


     def walk (self):
        return "Walking..."





class Dog(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

roger = Dog("Roger", 3)

print(roger.bark())  # Output: Woof!
print(isinstance(roger, Dog))  # Output: True
print(type(roger))  # Output: <class '__main__.Dog'>
print(f"Name: {roger.name}, Age: {roger.age}")  # Output: Name: Roger, Age: 3

print(roger.walk())  # Output: Walking...

