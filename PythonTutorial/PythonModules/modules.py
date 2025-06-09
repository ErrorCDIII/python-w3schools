# Modules

# What is a Module?

# The same as a code library
# A file containing a set of functions you want to 
# include in you application

# Create a Module

# To create a module just save the code in a file with
# the file extension .py

# For this exercise a module file named mymodule.py 
# was created

# Use a Module

# Now we can use the module (mymodule.py) we just
# created, by using the import statement

# Example: import the module named mymodule, and call
# the greeting function

import mymodule

mymodule.greeting("Jonathan")

# Syntax:
# module_name.function_name

# Variables in Module

# The module can contain functions, but also variables
print()

a = mymodule.person1["age"]
print(a)

# Re-naming a Module

# You can create an alias when you import a nmodule
# by using the as keyword

import mymodule as mx

print()

a = mx.person1["country"]
print(a)

# Build-in Modules

import platform

print()

x = platform.system()
print(x)

# Using the dir() Function
# There is a bluit-in function to install the function
# names (or the variable names) in a module
# The dir() function:

# Example: List all the defined names belonging to the
# platform module

import platform

print()

x = dir(platform)

print(x)
# Note: the dir() function cal be used on all modules,
# also the ones you create yourself

# Import From Module

# You can choose to import only parts from a module,
# by using the form keyword

# Example: the module named mymodule has one function
# and one dictionary.
# Import only yhe person1 from said module:
from mymodule import person1

print()

print(person1["name"])
# Note: When importing using the from keyword, do not 
# use module name when referring to elements in the module.