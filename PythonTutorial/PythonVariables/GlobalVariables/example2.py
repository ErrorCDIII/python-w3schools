# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)
# Uses local scope

myFunc()

# Uses global scope
print("Python is " + x)