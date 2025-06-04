# Loop Through a Dictionary
# Using a for loop
# When looping through a dictionary, the return value are the 
# keys of the dictionary, but there are methods to return values as well

thisdic = {
    "name": "Paulo",
    "age": 39
}

for x in thisdic:
    # print(x)
    # print(thisdic[x])
    print(f"{x} - {thisdic[x]}")

print()

# You can use the values() method to return values of a dictionary
for x in thisdic.values():
    print(x)

print()

# You can use the keys() method to return the keys oif a dictionary
for x in thisdic.keys():
    print(x)

print()

# Loop through both keys and values by using the items() method:
for x, y in thisdic.items():
    print(x, y)