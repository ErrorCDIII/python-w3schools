# Access Items

# List items are indexed and you can access them by referring to the index number
thisList1 = ["apple", "banana", "cherry"]
print(thisList1[1])
# Note: The first item has index 0.

# Negative Indexing
# Negative indexing means start from the end of the list
print(thisList1[-1])
# -1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thisList2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList2[2:5])
# Remember that the first item has index 0.
# The search will start at index 2 (included) and end at index 5 (not included).

# y leaving out the start value, the range will start at the first item
print(thisList2[:4])

# By leaving out the end value, the range will go on to the end of the list
print(thisList2[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list
print(thisList2[-4:-1])

print()

# Check if Item Exists

# To determine if a specified item is present in a list use the in keyword
thisList3 = ["apple", "banana", "cherry"]
if "apple" in thisList3:
    print("yes, 'apple' is in the fruits list")