# for Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop doesn't require an indexing varialbe

# Looping Through a String
print()

for x in "banana":
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all items
print()
for x in fruits:
    print(x)
    if x == "banana":
        break

print()
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next
print()
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function

# To loop through a set of code a specified number of times,
# we can use the range() function.

# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1
# (be default), and ends at the specified number
print()
for x in range(6):
    print(x)
# Note: the range(6) represents the values of 0 to 5

# The range function defaults to 0 as a starting value, 
# however it is possible to specify value (start and end)
# It is starting value inclusive and ending value non-inclusive
print()
for x in range(2, 6):
    print(x)
# 2 is included and 6 is not

# The range() function defaults to increment the sequence by 1
# however it is possible to specify the increment step
print()
for x in range(2, 30, 3):
    print(x)

# else in for Loop
# The else keuword in a for loop specifies a block of code
# to be executed when the loop is finished
print()
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# Note: the else block will NOT be executed if the loop 
# is stopped by a break statement

print()
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Nested Loops
# A nested loop is a loop inside another loop
# The "inner loop" will be executed one time
# for each iteration of the "outer loop"
print()
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason
# have a for loop with no content, put in the pass
# statement to void getting errors
print()
for x in [0, 1, 2]:
    pass