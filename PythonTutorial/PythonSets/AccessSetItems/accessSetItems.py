# Access Set Items

# You cannot access items in a set by referring to an index or a key
# You can loop through the set items using a loop or 
# asking if a specified value is present in a set 
# using the in keyword
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)
# Returns a Boolean
print("banana" not in thisset)

# Change Items
# Once a set is created, you cannot change it's items, but you can add new items