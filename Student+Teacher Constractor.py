class Person:
    def __init__(self, name, age):
        # Parameterized constructor initializes 'name' and 'age' attributes
        self.name = name
        self.age = age

# Creating objects of the Person class with specific values
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes of the objects
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")
