# Loop Through a List
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by refering to their index number.
# Use the range() and len() functions to create a suitable iterable.
print()
for i in range(len(thisList)):
    print(thisList[i])
# The list length is 3
# The range() function generates the iterable [0, 1, 2]
# Those values are assigned as indexes to access the list's values

# Using a While Loop
print()
i = 0
while i < len(thisList):
    print(thisList[i])
    # i = i + 1
    # Python não tem operador de incremento/decremento
    i += 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists
print()
[print(x) for x in thisList]