# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regerdless of the 
# result of the try-and except blocks

# Exception Handling

# When an errors occurs, or exception as we call it, Python will
# normally stop and generate an error message.

# These exceptions can be handled using the try statement

try:
    print(x)
except:
    print("An exception occurred")

# Since the try block raises an error, the except block will 
# be executed
# Without the try block, the program will crash and raise an error

# In the example above, print(x) will raise an error because
# x is not defined

# Many Exceptions

# You can define as many exception blocks as you want

# Example: print one message if the try block raises a NameError
# and another for other errors:
print()

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")

# Else

# You can use the else keyword to define a block of code to be 
# executed if no errors were raised:

print()

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally

# The finally block, is specified, will be executed regardless 
# if the try block raises an error or not

print()

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# This ca be useful to close objects and clean up resourses:

# Example: try to open and write a file that is not writable:

print()

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# The program will continue, without leaving the file object open

# Raise an exception
# You can choose to throw an exception if a condition accurs
# To do so, use the raise keyword

# Example: raise an error and stop the program if x is lower than 0

print()

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# You can define what kind of error to raise, and the text to 
# print to the user

# Example: raise a TypeError if x is not an integer:

print()

x = "Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")