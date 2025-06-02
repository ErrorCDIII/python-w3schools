# Copy a List

# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be 
# made in list2.

thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(thisList)
print(myList)

print()

# Use the list() method
# Another way to make a copy is to use the built-in method list()
thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
print(thisList)
print(myList)

print()

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator
thisList = ["apple", "banana", "cherry"]
myList = thisList[:]
newList = thisList[1:]
# Starts the copy process at the element number 1 which is "banana"
# and continues untill the end of the lists
print(myList)
print(thisList)
print(newList)