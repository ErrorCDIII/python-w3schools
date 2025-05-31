# The remove() method removes the specified item.
# Remove "banana"
thisList = ["apple", "banana", "cherry"]
print(thisList)
thisList.remove("banana")
print(thisList)

# If there are more than one item with the specified value, the remove() method removes the first occurence
newList = ["apple", "banana", "cherry", "banana", "kiwi"]
print()
print(newList)
newList.remove("banana")
print(newList)

# Remove Specified Index
# The pop method removes the specified index
thisList2 = ["apple", "banana", "cherry"]
print()
print(thisList2)
thisList2.pop(1)
print(thisList2)

# If the index is not specified, the pop() methods removes the last item.
print()
newList2 = ["apple", "banana", "cherry"]
print(newList2)
newList2.pop()
print(newList2)

# The del keyword also removes the specified index
thisList = ["apple", "banana", "cherry"]
print()
print(thisList)
del thisList[0]
print(thisList)
del thisList
# print(thisList)
# This would generate an error because the list no longer exists

# Clear the List
# The clear() method empties the list
# The list still remains, but has no content
thisList = ["apple", "banana", "cherry"]
print()
print(thisList)
thisList.clear()
print(thisList)