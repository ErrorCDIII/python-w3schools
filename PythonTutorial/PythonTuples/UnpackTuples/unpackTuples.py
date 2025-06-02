# Unpacking a Tuple
# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple

# Example: packing a tuple
fruits = ("apple", "banana", "cherry")

# We are also aloowed to extract values from tuples back into variables.
# This process is called "unpacking"

# Example: unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# Note: The number os variables must match the number os values in the tuple,
# if not, you must use an asterisk to collect the remaining valies as a list

# Using Asterisk *
# If the number of variables is less than the nu,ber of values,
# you can add an * to the variable name and the values will be assigned
# to the variable as a list

print()

# Example: assign the rest of the values as a list called "red"
fruist = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
# red is a list of strings

print(green)
print(yellow)
print(red)
print(type(red))
# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable untill the number 
# of values left matches the number of variables left

print()

# Example: add a list of values to the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(type(green))
print(tropic)
print(type(tropic))
print(red)