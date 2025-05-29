class myClass():
    def __len__(self):
        return 0
    
myobj = myClass()
print(bool(myobj))

# Functions can return a Boolean
def myFunction():
    return True

print(myFunction())

# You can execute code based on the Boolean answer of a function:
print()

if myFunction():
    print("YES!")
else:
    print("NO!")

print()

# Python also has many built-in functions that return a boolean value
# The function isinstance() can be used to determine if an object is of a certain data type
# and returns a Boolean
x = 200
print(isinstance(x, int))