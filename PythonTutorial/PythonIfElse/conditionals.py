# If ... Else

# Python Conditions and If Statements
    # Equals: a == b
    # Not Equals: a != b
    # Less Than: a < b
    # Less Than or Equal: a <= b
    # Greater Than: a > b
    # Greater Than or Equal: a >= b

a = 33
b = 200
if b > a:
    print("b is greater than a")

# Indentation
# Python relies on indentation to define scope
print()

a = 33
b = 200
# if b > a:
# print("b is greater than a")
# This will generate an error

# if b > a:

# print("b is greater than a")
# This will also generate an error

# Elif
# The elif keyword means: "if the previous conditions were not tur, then evaluate this condition"

print()

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions
print()

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short hand If
# if you have only one statement to execute, you can
# put it on the same line as the if statement

print()

if a > b: print("a is greater than b")

# Short Hand If ... Else
# You can only have one statement to execute, one for if, and one for else
# you can put it all on the same line

print()

a = 2
b = 330
print("A") if a > b else print("B")
# This technique is known as Ternary Operators, or Conditional Expressions

# You can also have multiple else statements on the same line:

print()

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements

print()

# Example: test if a is greater than b, AND if c os greater than a
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements

# Example: test if a is greater than b, OR if a is greater than c
print()

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At last one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement

# Example: test if a is NOT greater than b
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If
# You can have if statements inside other if statements, this is called nested of statements
print()

# Example
x = 41

if x > 10:
    print("Above then,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannor be empty, but if you for some reason
# have an if statement with no content, put in the pass
# statement to avoid getting an error

print()

a = 33
b = 200

if b > a:
    pass