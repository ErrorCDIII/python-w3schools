# Change Values
# You can change the vale of a specific item by referring to ti's key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["year"])

thisdict["year"] = 2018
print(thisdict["year"])

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument
# The argument must be a dictionary, or an iterable object with key:value pairs

print()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

thisdict.update({"year": 20202})

print(thisdict)