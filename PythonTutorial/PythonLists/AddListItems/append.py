# To add an item to the end of a list, use the append() method
thisList = ["apple", "banana", "cherry"]
print(thisList)
thisList.append("orange")
print(thisList)

# To insert a list item at a specified index, use the insert() method
# The insert method inserts an item at the specified index
thisList2 = ["apple", "banana", "cherry"]
print(thisList2)
thisList2.insert(1, "orange")
print(thisList2)
# This will increse the lit's length

# Extend List
# To append elements from another list to the current list, use the extend() method
fruits = ["apple", "banaba", "cherry"]
tropicalFruits = ["mango", "pineapple", "papaya"]
print(fruits)
fruits.extend(tropicalFruits)
print(fruits)
# This will not create a copy of the orignial list but instead change it

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object
# (tuples, sets, dictionaries, etc)
newList = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
print()
print(newList)
newList.extend(thisTuple)
print(newList)