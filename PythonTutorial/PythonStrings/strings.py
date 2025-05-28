print("Hello")
print('Hello')

# Quotes inside quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string
a = 'Hello'
print(a)

# Multiline Strings
# String literal
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
# Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays (0 based)
c = 'Hello World'
print(a[1])     # e

# Looping through a string
for x in "banana":
    print(x)

# String Length
c = "Hello, World"
print(len(c))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# It returns a bool
txt = "The best things in life are free!"
print("free" in txt)

# In an if statement:
txt2 = "The best things in life are free!"
if "free" in txt2:
    print("Yes, 'free' is present.")

# Check if Not
txt3 = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")