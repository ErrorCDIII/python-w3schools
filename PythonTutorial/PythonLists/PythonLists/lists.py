myList = ["apple", "banana", "cherry"]

# Lists are used to store multiple items in a single variable.

print(myList)

thisList = ["orange", "something", "something"]
print(thisList)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Since lists are indexed, lists can have items with the same value

newList = ["apple", "banana", "cherry", "apple", "cherry"]
print(newList)

# List Length
# To determine how many items a list has, use the len() function
print(len(newList))

# List Items - Data Types
# List items can be of any data type

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# A list can contain different data types
list4 = ["abc", 34, True, 40, "male"]

# From Python's perspective, lists are defined as objects with the data type 'list'
print(type(list4))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list
thisList2 = list(("apple", "banana", "cherry"))
print(thisList2)