# Arrays

# Python does not have built-in support fo arrays, but
# lists can be used instead

# Note: This show how to use LISTS as ARRAYS, however,
# to work with arrays you'll have to import the NumPy library

# Arrays are used to store multiple values in one single variable

cars = ["Ford", "Volvo", "BMW"]

# What's an Array?

# An array is a special variables, which can hold more
# than one value at a time

# Arrays can hold many values under a single name, and you 
# can access them by referring to their index number

x = cars[0]

print(x)

# Modify the value of the first array item
cars[0] = "Toyota"

print()

print(cars)

# The Length of an Array

x = len(cars)

print()

print(x)

# Looping Array Elements
print()

for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array

print()

cars.append("Honda")

print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array
print()

cars.pop(1)

print(cars)

# You can also use the remove() method

print()

cars.remove("BMW")

print(cars)
# Note: The remove() method only removes the FIRST
# occurrence of the specified value

# Array Method

# Method      Description
# append()    Adds an element at the end of the list
# clear()     Removes all elements from the list
# copy()      Returns a copy of the list
# count()     Returns the number of elements with the specified value
# extend()    Add the element of a list (or iterable) to the end of the current list
# index()     Returns the index of the first element with the specified value
# insert()    Add an element at the specified position
# pop()       Removes the element at the specified position       
# remove()    Removes the first item with the specified value
# reverse()   Reverses the order of the list
# sort()      Sorts the list
