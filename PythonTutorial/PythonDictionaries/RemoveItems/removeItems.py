# Removing Items
# The pop() method removes the item with the specified key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
# In earlier versions it removes a random item
print()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specifed key name
print()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
del thisdict["model"]
print(thisdict)

print()

# The del keyword can also delete a complete dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

del thisdict
# print(thisdict)
# This will generate an error

print()

# The clear() method empties the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

thisdict.clear()

print(thisdict)