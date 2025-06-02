# Remove Set Items
# To remove an item in a set, use the remove(), or the disxard() method
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)

# Note: if the item to remove does not exist, remove() will raise an error
print()

thisset = {"apple", "banana", "cherry"}
thisset.discard("clementine")
print(thisset)

# Note: if the item to remove does not exit, discard() will not cause an error

# You can also use the pop() method to remove an item,
# but this method will remove a random item

print()

# Example: remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)
# The return value of the pop() method is the removed item

# The clear() method empties a set
print()

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.clear()
print(thisset)
# The result is set()

# The del keyword will delete the set completely
print()

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)
# This will raise an error since the set no longer exists