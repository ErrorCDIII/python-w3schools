# Functions

# A function is a code of block which only runs when it is called
# You can pass data, know as parameters, into a function
# A function can return data as a result

# Creating a Functions
# A function is defined using the def keyword
def my_function():
    print("Hello form a function")

# Calling a Function
my_function()

# Arguments
# Information can be passed into functions as arguments
# Arguments are specified after the funcion name, 
# inside parentheses. You can add as many arguments as 
# you want, just seperate them with a comma.

print()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
# The terms parameter and argument can be used for the same 
# thing: information that is passed into a function.

# An argument is a realization of a paramter.
# A parameter is a variable passed to a function in it's 
# definition, while an argument is a value passed to a 
# function when it is called

# Number of Arguments

print()
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# This function expects 2 arguments, but only gets 1
print()
def my_function(fname, lname):
    print(fname + " " + lname)

# my_function("Emil")
# This will generate an error
# TypeError: my_function() missing 1 required positional argument: 'lname'

# Arbitrary Arguments, *args
# if you do not know how many arguments that will be 
# passed into your function, add a * before the parameter 
# name in it's definition

# This way the function will receive a tuple of arguments,
# and can access them accordingly
print()
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter
print()
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will
# be passed into your function, add two asterisks:
# ** before the parameter name in the funcion definition.

# This way the function will receive a dictionary of 
# arguments, and can access them accordingly
print()
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# If we call the fuction without arguments, it uses the 
# default value, if it is defined in it's signature
print()

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
print()

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
# To let a function return a value, use the return statement
print()

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
# function definitions connot be empty, but if you for 
# some reason have a function definition with no content, 
# put in the pass statement to avoid errors
def my_function():
    pass

# Positional-Only Arguments
# You can specify that a function can ONLY have positional
# arguments, or ONLY keyword arguments

# To specify that a function can have only positional 
# arguments, add , / after the arguments
print()

def my_function(x, /):
    print(x)

my_function(3)

# Without the , / you are actually allowed to use keyword 
# arguments even if the funcion expects positional arguments
print()

def my_function(x):
    print(x)

my_function(x = 3)

# But when adding the , / you will get an error if you 
# try to send a keyword argument
print()

def my_function(x, /):
    print(x)

# my_function(x = 3)
# This will generate an error
# TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, 
# add *, before the arguments
print()

def my_function(*, x):
    print(x)

my_function(x = 3)
# my_function(3)
# This will raise an error
# TypeError: my_function() takes 0 positional arguments but 1 was given

# Combine Positional-Only and Keyword-Only Arguments
# You can combine the wto argument type
print()

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion
# When a function calls itself
print()

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)