# Add Items
# Once a set is created, you cannot change it's items,
# but you can add new ones
# To add an item to a set use the add() method
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

# Add Sets
# To add items from another set into the current one,
# use the update() method
print()

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

print(thisset)
thisset.update(tropical)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be
# a setm ir can be any iterable object
# (tuples, lists, dictionaries, etc) 
print()

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

print(thisset)

thisset.update(mylist)
print(thisset)