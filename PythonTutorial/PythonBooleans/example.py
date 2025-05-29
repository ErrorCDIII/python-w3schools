# Booleans

# Booleans represent one fo two value: True or False
# When you compare two values, the expression is evaluated and Python returns the Boolean answer

print(10 > 9)
print(10 == 9)
print(10 < 9)

print()

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, 
# and give you True or False in return

print()

print(bool("Hello"))
print(bool(15))

# Almost any value is evaluated to True if it has some sort of content
# Any nymber, except 0 is True
# Any list, tuple, set, and dictionary are True, except empty ones
print()

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# False Values
# False, Nome, 0 and empty values such as: (), [], {}, ""

print()

# The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))