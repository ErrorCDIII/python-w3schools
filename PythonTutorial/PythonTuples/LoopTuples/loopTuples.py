# Loop Through a Tuple

# Example: Iterate through the items by using a for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable

# Example: print all items by referring to their index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Using a While Loop
# You can loop through the tuple items by using a while loop
# Use the len() function to determine the length of the tuple,
# then start at 0 and loop your way through the tupe items by referring 
# to their indexes
# Increase the index by 1 after each iteration

print()

# Example: print all items, using a while loop to go through all the index numbers
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
    # i = i + 1