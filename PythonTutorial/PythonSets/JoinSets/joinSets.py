# Join Sets

# The union() and uptade() methods join all items from both sets
# The intersection() method keeps only the duplicates
# The difference() method keeps the items from the first set that are not in the other set(s)
# The symmetric_difference() method keeps all items EXCEPT the duplicates

# Union
# The union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set1)
print(set2)
print(set3)

print()

# Using the | operator instead of the union() method will produce the same result
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

print()

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets
# When using a method, just add more sets in the parentheses, separated by commas
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)

print(myset)

print()

# When using the | operator, seperate the sets with more | operators

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

print()

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# Note: the | operator only allows you to join sets with sets, and not with other data types like you can with union()

print()

# Union
# The update() method inserts all items from one set into another
# It changes the original set and does not return a nerw one
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# Note: both union() and update() will exclude any duplicate items

print()

# Intersection
# Keeps ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# Note: the & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method

print()

# The intersection_update() method will kepp ONLY the duplicates
# but it will change the original set instead of creating a new one
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

print()

# The values True and 1 are sonsidered the same
# The same goes for False and 0
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

print()

# Diference
# The diference() method will return a new set that will contain only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

print()

# You can use the - operator instead of the difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# Note: the - operator only allows you to join sets with sets, unlike the difference() method

print()

# The difference_update() method will also keep the items from the first set that are not in the other set,
# but will change the original set instead of returning a new one
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

print()

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

print()

# You can use the ^ operator instead of the symmetric_difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
# Note: the ^ operator only allows you to join sets with sets
# unlike the symmetric_difference() method

print()

# The symmetric_difference_update() method will also keep all but the duplicates
# but it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)