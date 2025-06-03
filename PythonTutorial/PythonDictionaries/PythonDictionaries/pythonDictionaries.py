thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Dictionary
# Used to store data values in key:value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates
# Used to be unordered but nowadays is ordered

# Dictionart Items
# Are ordered, changeable, and do not allow duplicates
# Can be reffered by using the key name

print()

print(thisdict["brand"])

# Changeable
# Meaning that we can change, add or remove items from it after it's creation

print()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# Dictionary Length
# We can use the len() function

print()

print(len(thisdict))

# Dictionary Items - Data Types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]    
}

print()
print(thisdict)

# type()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print()
print(type(thisdict))
print(type(thisdict["brand"]))
print(type(thisdict["model"]))
print(type(thisdict["year"]))

# The dict() COnstructor
print()

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

