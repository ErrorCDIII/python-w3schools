# Python Sets

myset = {"apple", "banana", "cherry"}

# Set

# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unindexed
# Note: Set items are unchangeable, but you cand add/remove items from it

# Example: create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: sets are unordered, so you cannot be sure in which order the items will appear

# Set Items
# Set items are unordered, unchangeable and do not allow duplicate values

# Unordered
# Meaning that the items in a set do not have a defined order
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key

# Unchangeable
# Meaning the we cannot change the items after the set has been created
# It is possible to add/remove items

# Duplicates Nor Allowed
# Sets cannor have two items with the same value
print()

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# While printing, the repeated values will be discarded
# Note: The values True and 1 are considered the same value in sets, and are treared as duplicates

print()

# Example: True and 1 are considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Note: The values False and 0 are considered the same in sets, and are treated as duplicates
# Example: False and 0 are considered the same value
print()

thisset = {"apple", "banana", "cherry", False, True, 0, 2}
print(thisset)

# Get the length of a set
print()

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type

# Example: string, int and boolean data types
print()

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

print()

# A set can contain different data types
setA = {"abc", 34, True, 40, "male"}
print(setA)

print()

# type()
# Sets are objects of the data type 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))

print()

# The set() Constructor
# Example: using a set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))
# note the double parenthesis
print(thisset)

# Python Collections (Arrays)
# There are four collection data types in Python:
#   List - a collection which is ordered and changeable.
#       Allows duplicate members
#   Tuple - a collection which is ordered and unchangeable.
#       Allows duplicate members
#   Set - a collection which is unordered, unchangeable and unindexed.
#       Allows adding/removing items
#       No duplicate members
#   Dictionary - a collection which is ordered and changeable.
#       Used to be unordered but it's ordered nowadays
#       No duplicate members