# Change Item Value
# To change the value of a specific item, refer to the index number
thisList = ["apple", "banana", "cherry"]
print(thisList)
print(thisList[1])
thisList[1] = "blackcurrant"
print(thisList[1])

print()

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
newList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(newList)
newList[1:3] = ["blackcurrant", "watermelon"]
print(newList)

print()

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thisList2 = ["apple", "banana", "cherry"]
thisList2[1:2] = ["blackcurrant", "watermelon"]
print(thisList2)
# The length of the list will change when the number of items inserted does not match the number of items replaced.

print()

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
newList2 = ["apple", "banana", "cherry"]
print(newList2)
newList2[1:3] = ["watermelon"]
print(newList2)

print()

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method
# The insert() method inserts an item at the specified index
thisList3 = ["apple", "banana", "cherry"]
print(thisList3)
thisList3.insert(2, "watermelon")
print(thisList3)
# This will increase the list's length