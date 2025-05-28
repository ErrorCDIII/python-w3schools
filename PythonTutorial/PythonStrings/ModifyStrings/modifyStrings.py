# Upper Case
a = 'Hello World'
print(a.upper())

# Lower Case
print(a.lower())

# Remove Whitespace
b = "Hello, World!    "
print(b.strip())    # returns "Hello, World!"

# Replace String
print(a.replace("H", "J"))  # returns "Jello, World!"

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator
c = "Hello, World!"
print(c.split(","))     # returns ['Hello', ' World']