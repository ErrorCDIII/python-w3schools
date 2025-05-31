# List Comprehension

# Example: based on a list of fruits, you want a new list, containing only the fruits 
# with the letter 'a' in it's name

# Without a list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
    
print(newList)
# Note: the indentation has meaning and can cause unexpected results:

print()

# With list comprehension you can do all that with only one line of code:
newFruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList2 = [x for x in newFruits if "a" in x]
print(newList2)

# The Syntax
# newList = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old one unchanged

# Condition
# The condition is like a filter that only accpets the items that evaluate to True
print()

newList3 = [x for x in fruits if x != "apple"]
print(newList3)

# The condition is optional and can be ommited
print()

newList4 = [x for x in fruits]
print(newList4)
print(fruits)
# This process will create a new list that's a copy, whithout altering the original one

# Iterable
# You can use the range() fucntion to create an iterable:
print()

myList = [x for x in range(10)]
print(myList)

# Example: Accept only numbers lower than 5:
print()

myList2 = [x for x in range(10) if x < 5]
print(myList2)

# Expression
# The expression is the current item in the iteration, but it is also
# the outcome, which you can manipulate before it ends up
# like a list item in the new list:

# Example: Set the values in the new list to upper case:
print()

myList3 = [x.upper() for x in fruits]
print(myList3)

# Example: Set all values in the new list to 'hello':
print()

newList = ['hello' for x in fruits]
print(newList)

# The expression can also contain conditions, not like a filter, 
# but as a way to manipulate the outcome:
# Example: Return "orange" instead of "banana":
print()

newList2 = [x if x != "banana" else "orange" for x in fruits]
print(newList2)