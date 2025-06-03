# Accessing Items
# You can access the items of a dicionary be referring to it's key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x)

# There is also a method called get()
print()

x = thisdict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in a dictionary
print()
x = thisdict.keys()
print(x)

# The list of keys is a view of the dicitonary, meaning any changes done
# to the dictionary will reflect in ths keys list
print()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)    # before the change

car["color"] = "white"

print(x)    # after the changes

# Get Values
# The values() method will return a list of all the values
print()

x = thisdict.values()
print(x)

# This is also a view of the dictionary and the same consequences apply
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print()

print(x)    # before the change

car["year"] = 2020

print(x)    # after the change

car["color"] = "red"

print(x)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list
print()

x = thisdict.values()
print(x)
# This also generates a view with the already described consequences

print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x)

car["color"] = "red"
print(x)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

if "model" in thisdict:
    print("Yesm 'model' is one of the keys in the thisdict dictionary")