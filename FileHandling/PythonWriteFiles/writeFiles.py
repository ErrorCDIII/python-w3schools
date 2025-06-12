# Write to an Existing File

# To write to an existing file you must add a parameter to the 
# open() function
#   "a" - Append - will append to the end of the file
#   "w" - Write - will overrite any existing content

# Example: open the file "demofile.txt" and append to the file

with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

with open("demofile.txt") as f:
    print(f.read())

# Overwrite Existing Content

# To overwrite the existing content to the filem use the "w" 
# parameter

print()

with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
    print(f.read())
# Note: the "w" method will overwrite the entire file

# Create a New File

# To create a new file, use the open() method, with one of the 
# following parameters:
#   "x" - Create - will create a file, returns error if the 
#       file exists
#   "a" - Append - will create a file if the specified files does
#       not exists
#   "w" - Write - will create a file if the specified file does
#       not exists

f = open("myfile.txt", "x")
# Note: If the file already exists, an error will be raised