# Match

# The match statement is used to perform different actions based on different conditions

# The Python Match Statement
# Instead of writing many if .. else statements, you can use the match statement
# The match statement selects one of many code blocks to be executed

# Syntax
# match expression:
#     case x:
#         code block
#     case y:
#         code block
#     case z:
#         code block

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Default Value
# The underscore character is used as catch-all value and should be the last value in a Python match
print()

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# The value _ will always match, so it is important to place it as the last case to make it behave as a default case

# Combine Values
# Use the pipe character | as on operator in the case evaluation to check for more than one value match in one case:

print()

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I lovve weekends!")

# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A 2eekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")