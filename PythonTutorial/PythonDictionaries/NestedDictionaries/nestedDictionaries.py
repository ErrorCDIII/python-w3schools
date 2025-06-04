# Nested Dictionaries

# A dictionary can contain dictionaries, this is called a nested dictionary

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Example: create three dictionaries, then create one doctionary that will
# contain the other three
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# Access Items in Nested Diciotnaries
# To access items from a nested dictionary, you use the name of the dictionaries,
# starting with the outer dictionary

# Example: print the name of child 2:
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
# You can loop through a dicitonary by using the items() method
print()

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
