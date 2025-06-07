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