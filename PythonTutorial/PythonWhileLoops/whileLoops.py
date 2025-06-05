# Python Loops

# Python has two primitive loop commands
#   while loops
#   for loops

# The while Loop
# Whith the while loop we can execute a set of statements as long as a condition is true
i = 1

while i < 6:
    print(i)
    i += 1
# The while loop requires relevant variables to be ready

# The break Statement
# With the break statement we can stop the
# loop event if the while condition is true

print()

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1