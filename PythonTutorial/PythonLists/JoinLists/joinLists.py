# Join Two Lists
# There are several ways to join, or concatenate lists

# One of the easiest ways is to use the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print()

# Another way is to append all items from one listo into the other
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

print(list1)

for x in list2:
    list1.append(x)

print(list1)

print()

# You can also use the extend() method, where the purpose is to add elements from one list to another
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

print(list1)

list1.extend(list2)
print(list1)