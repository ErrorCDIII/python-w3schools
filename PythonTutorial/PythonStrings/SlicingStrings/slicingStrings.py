# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included)
# Note: The first character has index 0.
b = "Hello, World"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
print(b[-5:-2])