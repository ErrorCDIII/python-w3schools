myTuple = ("apple", "banana", "cherry")

# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values
# Tuple items are indexed and they are zero based

# Ordered
# Meaning they have a defined orded, and that order will not change

# Unchageable
# Meaning one cannot change, add or remove items after the tuple has been created

# Allow Duplicates
# Since they are indexed, they can have items with the same value
print()

thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

print()

# Tuple Length
thisTuple = ("apple", "banana", "cherry")
print(len(thisTuple))

print()

# Create Tuples WIth One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thisTuple = ("apple",)
print(type(thisTuple))

thisTuple2 = ("apple")
print(type(thisTuple2))

# Tuple Items - Data Types
# Tuple items can be of any data type
print()

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False, 3)
print(tuple3)

print()

# Tuples can contain different data types
tuple4 = ("abc", 34, True, 40, "male")

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple'
# <class 'tuple'>

mytuple  = ("apple", "banana", "cherry")
print(type(mytuple))

print()

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Python Collection (Arrays)
# There are four collection data types in Python:
#   List: is a collection which is ordered and changeable.
#       Allows duplicate members
#   Tuple: is a collection which is ordered and unchangeable.
#       Allows duplicate members
#   Set: is a collection wich is unordered, unchangeable and unindexed.
#       Set items are unchangeable, but you can add/remove items.
#       No duplicate members
#   Dictionary: is a collection which is ordered and changeable.
#       Used to be unordered but are currently ordered.
#       No duplicate members