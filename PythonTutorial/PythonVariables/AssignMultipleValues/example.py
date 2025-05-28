x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
# x, y, z = "Orange" -> Genberates an error
# The correct syntax is:
x = y = z = "Orange"

print(x)
print(y)
print(z)

# Unpack a collection
# One can have a collection of values in a list, tuple, etc...
# Extracting values from them is called unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)