# Python Classes and Objects

# A class is like an object constructor, or a "blueprint"
# for creating objects

# Create a Class
# To create a class, use the class keyword
class MyClass:
    x = 5

# Create an Object
p1 = MyClass()
print(p1.x)

# The __init__() Function
# All classes have a function called __init__(), which 
# is always executed when a class is being initiated

# Use the __init__() function to assign values to object 
# properties, or other operations that are necessary to do 
# when the object is being created

# Example: create a class named Person, use the __init__()
# function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print()

print(p1.name)
print(p1.age)

# Note: the __init__() function is called automatically
# every time the class is being used to create a new object

# Note: self is a reference to the actual object.
# It connects the new object about to be created to the 
# properties (and their values) it's about to receive

# The __str__() Function
# The __str__() function controls what should be returned
# when the class object is represented as a string

# If the __str__() function is not set, the string 
# representation of the object is returned

# Example: the string representation of an objecy WITHOUT
# the __str__() function
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

# Example: the string representation of an object WITH the __str__() function
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 26)

print(p1.name)
print(p1.age)
print(p1)

# Object Methods
# They can also contain methods.
# Methods in objects are function that belong to the object itself

# Example: insert a function that prints a greeting, and 
# execute it on the p1 object
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello my name is " + self.name + ".")

p1 = Person("John", 36)
p1.myfun()

# Note: the self parameter is a reference to the current 
# instance of the class and is used to access variables 
# that belong to the class

# The self Parameter
# The self parameter is a reference to the current instance 
# of the class, and is used to access variables that 
# belong to said class

# It does not have to be named self, you can call it whatever 
# you like, but it has to be the FIRST parameter of any 
# function in the class


# Example: use the words mysillyobject and abc instead of self
print()

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name + ".")

p1 = Person("John", 36)
p1.myfunc()

# Modify Object properties
# You can modify properties on objects like so:
print()

print(p1)
print(p1.name)
print(p1.age)
p1.age = 40

print()

print(p1.name)
print(p1.age)
print(p1)

# Delete Object Properties
# You can delete properties ob ojects by using the del keyword
print()

del p1.age

print(p1.name)
# print(p1.age)
# This will generate an error, since the age property no longer exists

# Delete Objects
# You can delete objects by using the del keyword
print()

del p1
# print(p1)
# This will raise an error since p1 doesn't exist anymore

# The pass Statement

# class definitions cannot be empty, but if for some 
# reason you have a class definition with no content,
# put in the pass statement to avoid error
class Person:
    pass