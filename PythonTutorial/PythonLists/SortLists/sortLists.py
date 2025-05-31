# Sort List Alphanumerically

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thisList)
print(thisList.sort())
# This returns None
# Since the method sort() changes the original list 
# "in-place" and has no value to return
# It returns None as an indication that the operation 
# (sorting in this case) was completed
thisList.sort()
print(thisList)

print()

luckyNumbers = [100, 50, 65, 82, 23]
print(luckyNumbers)
luckyNumbers.sort()
print(luckyNumbers)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
print()

print(thisList)
thisList.sort(reverse=True)
print(thisList)

print()

print(luckyNumbers)
luckyNumbers.sort(reverse=True)
print(luckyNumbers)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list
# (lowest number first)
print()

# Example: Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myfunc)
print(thisList)
thisList.sort(key=myfunc, reverse=True)
print(thisList)

# Case Insensitive Sort
