# Open Files

# Open a File on the Server

# Assume you have the following file, located in the same folder
# as Python

# demofile.txt
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# To open the file, use the built-in open() function

# The open() function returns a file object, which has a read()
# method for reading it's content

f = open("demofile.txt")
print(f.read())

# If the file is located in a different location, you will
# have to specify the file path

print()

f = open("./demofile.txt")
print(f.read())

# Using the with Statement

# You can also use the with statement when opening a file

# Example: using th with keyword

print()

with open("demofile.txt") as f:
    print(f.read())
# You don't have to worry about closing your files, the with 
# statement takes care of that

# Close Files

# It is good pratice to always close the file when you are done 
# with it.

# if you are not using the with statement

# Acording to chatGPT:
# The with statement in Python is used to manage contexts, 
# especially when working with resources that need to be opened 
# and then properly closed — such as files, network connections, 
# or databases.

# Example: close the file when you are finished with it

print()

f = open("demofile.txt")
print(f.readline())
print(f.read())
print(f.readlines())
f.close()

# Note: you should always close your files. In some cases, due to 
# buffering, changes made to a file may not show until you close 
# the file

# Read Only Parts of the File