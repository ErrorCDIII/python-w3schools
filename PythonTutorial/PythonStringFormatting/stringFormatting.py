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

print()

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# Formatting Types
# :<  Left aligns the result
# :>  Right aligns the result
# :^  Center aligns the result
# :=  Places sign to the left most position
# :+  Use the plus sign to indicate if the result is positive or 
#     negative
# :-  Use the minus sign to indicate negative values only
# :   Use a space to insert an extra space before positive numbers
# :,  Use a comma as a thousand separator
# :_  Use underscore as a thousand separator
# :b  Binary format
# :c  Converts the value into the corresponding Unicode character
# :d  Decimal format
# :e  Scientific format, with a lower case e
# :E  Scientific format, with a upper case e
# :f  Fix point number format
# :F  Fix point number format, in uppercase format
# :g  General format
# :G  General format (using upper case E for scientific notations)
# :o  Octal format
# :x  Hex format, lower case
# :X  Hex format, upper case
# :n  Number format
# :%  Percentage format

# String format()

# Before Python 3.6, we used the format() method 
# It can still be used and it also uses curly brackets as placeholders

# Example: add a placeholder where you want to display the price

print()

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# You can add parameters inside the curly brackets to specify 
# how to convert the value

# Example: format the price to be displayed as a number with two decimals
print()

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values

# If you want to use more values, just add more values to the
# format() method 

print()

itemno = 30
count = 5

print(txt.format(price, itemno, count))

# And add more placeholders

print()

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers

# You can use index numbers (a number inside the curlt brackets)
# {0} to be sure the values are placed inthe correct placeholders

# Example:

print()

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Alse, if you want to refer to the same value more than once,
# use the index number:

# Example:

print()

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes

# You can also use named indexes by entering a name inside the
# curly brackets {carname}, but then you must use names when you
# pass the parameter values txt.format(carname = "Ford")

# Example:

print()

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))