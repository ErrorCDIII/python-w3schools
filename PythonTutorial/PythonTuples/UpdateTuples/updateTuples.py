# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created
# But there are some workarounds

# Change Tuple Values
# Once a tuple is created, you cannot change its values.
# Tuples are unchangeable or immutable.
# You can convert a tuple into a list, change the list, and convert the list back into a tuple

# Example: convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print(y)

# Add Items

# Since tuples are immutable, they do not have a built-in append() method, but there are ways to add items to a tuple

print()

# 1 - Convert into a list
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print()

# 2- Add tuple to a tuple
# You are allowed to add tuples to tuples.
# Create a new tuple with the items and add it to the existing tuple
# Example: create a new tuple with the value "orange" and add that tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = ("orange",)
thistuple += y

print(thistuple)
# Note: when creating a tuple with only one item, you have to add a ',' at the end so that it is considered a tuple and not a string

print()

# Remove Items
# Note: you cannot remove items in a tuple
# Typles are unchangeable, so you cannot remove items from it.
# The string workaround can still be use though
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

print()

# Or you can delete tue tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)
# This will raise an error because the tuple no longer exists

print()

# Python allows for empty tuples
# You can also convert into a list and clear it and convert into a tuple once again
thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.clear()
thistuple = tuple(y)
print(thistuple)