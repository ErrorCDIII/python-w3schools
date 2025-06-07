# Python Iterators

# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, 
# meaning that tou can traverse through all the values.

# In Python, an iterator is an object which implements 
# the iterator protocol, which consists of the methods
# __iter__() and __next()

# Iterator vs Iterablue

# Lists, tuples, dicitonaries and sets are all iterable 
# objects. They are iterable containers which tou can
# get an iterator from.

# All these objects have a iter() method which is used
# to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(myit)
# <tuple_iterator object at 0xffff94c70ee0>
print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, and can return an iterator
print()

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
# We can use a for loop to iterate through an iterable object
print()

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

print()

mystr = "banana"

for x in mystr:
    print(x)
# The for loop actually creates an iterator object and 
# executes the next() method for each loop 

# Create an Iterator
# To create an object/class as an iterator you have to
# implement the methods __iter__() and __next__()
# to your object

# All classes have a function called __init__(), which 
# allows you to do some initializing when the object
# is being created

# The __iter__() method acts similar, you can do operations
# (initializing, etc...) but must always return the 
# iterator object itself

# The __next()__ method also allows you to do operations,
# and must return the next item in the sequence

# Example: create an iterator that returns numbers, 
# starting whe 1, and each sequence will increase by one
print()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
# The example above would continue forever if you had 
# enough next() statements, or if it was used in a for loop

# To prevent the iteration form going forever, use the
# StopIteration statement

# In the __next__() method, we can add a terminating 
# condition to raise an error if the iteration is done a 
# specified number of times

print()

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)