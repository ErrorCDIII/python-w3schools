# Polymorphism

# Function Polymorphism

# An example of a function that can be used on different
# objects is the len() function

# String
x = "Hello World!"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

# Dictionary
# For dictionaries leng() retuns the number of key/value pairs
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1064
}
print(len(thisdict))

# Class Polymorphism
# Is often used in Class methods, where we can have 
# multiple classes with the same method name

# Example: say we have three classes; Car, Boat and Plane
# and they all have a method called move()
print()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")           # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")     # Create a Boat object
plane1 = Plane("Boeing", "747")         # Create a Plane object

for x in (car1, boat1, plane1):
    print(x)
    x.move()

# Because of polymorphism we can execute the same method
# for all three classes

# Inheritance Class Polymorphism
# Example: create a class called Vehicle and make Car, 
# Boat, Plane, child classes of Vehicle
print()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x)
    print(x.brand)
    print(x.model)
    x.move()

# Child classes inherit the properties and methods from 
# the parent class.

# In the example above you can see the Car class is empty,
# but it inherits brand, model and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, 
# and move() from Vehicle, but both override the move() method

# Because of polymorphism we can execute the same method for all classes