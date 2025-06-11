# Python String Formatting

# F-String is the preferred way of formatting strings.
# Before Python 3.6 we had to use the format() method.

# F-Strings

# F-Strings allow you to format selected parts of a string
# To specify a string as an f-string, simpy put an f in front
# of a string literal:

# Example: create an f-string

txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers

# To format values in an f-string, add placeholders {}
# A placeholder can contain variables, operations, functions,
# and modifiers to format the value

print()

# Example: add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value

# A modifier is included by adding a colon : fowllowed by a 
# legal formatting type, like .2f which means fixed point 
# number with 2 decimals:

# Example: display the price with 2 decimals:

print()

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# You can also format a value directly without keping it in a variable:

# Example: display the value 95 with 2 decimals

print()

txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform Operations in F-Strings

# You can perform operations inside the placeholders, 
# like math operations

# Example: perform a math operation in the placeholder, and return the result:

print()

txt = f"The price is {20 * 59} dollars"
print(txt)

# You can perform math operations on variables:

# Example: add taxes before displaying the price:

print()

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# You can perform if...else statements inside the placeholders

# Example: return "Expensive" if the price is over 50, otherwise
# return "Cheap"

print()

price = 49
txt = f"It is very {'Expensive' if price >50 else 'Cheap'}"
print(txt)

# Execute Functions in F-Strings

# You can execute functions inside the placeholder

# Example: use the string method upper() to conver a value
# into upper case letters:

print()

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# The function doesn't have to be a built-in Python method

# Example: crate a function that converts feet into meters:

print()

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# More Modifiers

# There are several modifiers that can be used to format values
# other than .2f

# Example: use a comma as a thousand seperator
