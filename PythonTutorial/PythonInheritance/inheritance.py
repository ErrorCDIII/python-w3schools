# Inheritance

# Inheritance allows us to define a class that inherits 
# all the methods and properties from another class

# Concepts:
# Parent Class:
#   is the class being inherited from, also called base class
# Child Class:
#   is the class that inherits from another class,
# also called derived class

# Create a Parent Class
# Any class can be a parent class, so the syntax is the 
# same as creating any other class

# Example: create a class named Person, with firstname
# and lastname properties, and a printname method:
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Create a Child Class
# To create a class that inherits the functionality from 
# another class, send the parent class as a parameter
# when creating the child class

# Example: create a class named Student, which will 
# inherit the properties and methods from the Person class
class Student(Person):
    pass
# Note: use the pass keyword when you do not want to add
# any properties or methods to the child class

# Now the Student class has the same properties and methods
# as the it's parent class (Person)

# Example: use thr Student class to create an objet,
# and then execute the printname method
x = Student("Mike", "Olsen")

print()
x.printname()

# Add the __init__() Function
# So faz we've created a child class tha inherits the 
# properties and methods from it's parent

# We want to add the __init__() function to the child class
# instead of the pass keyword

print()

class Student(Person):
    def __init__(self, fname, lname):
        pass
        # add properties, methods...

# When you add the __init__() function, the child class
# will no longer inherit the parent's __init__() function

# Note: the child's __init__() function OVERRIDES the
# inheritance of the parent's __init__() function

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function
# and ketp the inheritance of the parent class, and we
# are ready to add functionality in the __init__() function

# Use the super() Function
# Python also has the super() function that will make the 
# child class inherit all the methods and properties from it's parent
print()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# By using the super() function, you do not have to use
# the name of the parent element, it will automatically
# inherit the methods and properties from it's parent

# Add Properties
# Example: add a property called graduationyear to the Student class
print()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen", 2019)
print(x)

# Add Methods
# Example: add a method called welcome to the Student class
print()

class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x = Student("Paulo", "Melo", 2005)

x.welcome()

# If you add a method in the child class with the same 
# name as a function in the parent class, the inheritance
# of the parent method will be overridden