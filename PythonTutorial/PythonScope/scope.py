# Scope

# A variable is only available from inside the region
# it is creatd. This is called scope.

# Local Scope
# A variable created inside a function belongs to the 
# local scope of that function, and can only be used 
# inside said function
def myfunc():
    x = 300
    print(x)

myfunc()

# Function Inside Function
# The variable x in not availabe outside of the function
# bit it is available for any function inside the function
print()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope

# A variable created in the main body of the code is a 
# global variable and belongs to the global scope

# Global variables are availabe from within any scope,
# global and local

print()

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Naming Variables

# If you operate with the same variable name inside and 
# outside of a function, Python will treat them as two seperate variables,
# one available in the global scope and one available
# in the local scope

print()

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

# global Keyword

# If you need to create a global variable, but are 
# stuck in the local scope, use the global keyword.
# The global keyword makes the variables global.

print()

def myfunc():
    global x
    x = 300

myfunc() 

print(x)

# Also, use the global keyword if you want to make a change 
# to a global variable inside a function

print()

x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)

# nonlocal Keyword

# The nonlocal keyword is used to work with variables
# inside nested functions

# The nonlocal keyword makes the variable belong to the
# outer function

# Example: use the nonlocal keyword, the variable will
# belong to the outer function

print()

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())