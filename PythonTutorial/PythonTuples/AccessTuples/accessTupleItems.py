# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
# Note: tuples are zero-based

print()

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last...
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print()

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the rage
# The result will be a new tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[2:5])

print()

print(thistuple[:4])
print(thistuple[3:])
print(thistuple[2:4])

print()

# Range of Negative Indexes
# Specify negative indexes if you want to start to search from the end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


print()
# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
