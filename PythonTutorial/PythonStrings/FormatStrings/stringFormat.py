#  We can combine strings and numbers by using f-strings or the format() method!

# This will generate an error
# age = 36
# txt = "My name is John, I am " + age

# F-Strings
# String interpolation
# To specify a string as an f-string, simply put an f 
# in front of the string literal, and add curly brackets 
# {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}."
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions 
# and modifiers to formar the value
price = 59
txt2 = f"The price is {price} dollars."
print(txt2)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type
# .2f means fixed point number with 2 decimals
newPrice = 59
newTxt = f"The price is {price:.2f} dollars."
print(newTxt)

# A placeholder can contain Python code, like math operations
newTxt2 = f"The price is {20 * 59} dollars."
print(newTxt2)