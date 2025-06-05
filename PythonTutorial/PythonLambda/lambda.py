# Lambda

# A lambda function is a small anonymous function
# It can take any number of argumens, but can only have
# one expression

# Syntax
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

print()

x = lambda a, b : a * b
print(x(5, 6))

print()

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions
# For instance, they are useful when creating functions inside other function
print()

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
# This is like currying
# It is, in fact a higher order function using partial application

# Higher-Order Function
# It's a function that either receives a fuction as an 
# argument or returns a function

print()

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print()

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is
# required for a short period of time