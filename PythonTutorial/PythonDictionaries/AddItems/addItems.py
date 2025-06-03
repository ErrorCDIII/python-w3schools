# Adding Items
# Adding an item to a dictionary is done by using a
# new index key and assigning a balue to it
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

thisdict["color"] = "red"

print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument
# If the item does not exist, it'll be added
# The argumento must be a dictionary, or an iterable object with key:value pairs

print()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"color": "red"})