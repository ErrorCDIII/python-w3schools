# File Handling

# The key function for working with files is the open() function
# It takes two parameters: filename, and mode

# There are four different methods (modes) for opening a file:
#   "r" -> Read - Default value. Opens a file for reading, error
#       if the files does not exist
#   "a" -> Append - Opens a file for appending, creates the file 
#       if it does not exist
#   "w" -> Write - Opens a file for writing, creates the file
#       if it does not exist
#   "x" -> Create - Creates the specified file, returns an error
#       if the file already exists

# In addition you can specify if the file should be handled as
# a binary or text mode
#   "t" -> Text - Default value. Text mode
#   "b" -> Binary - Binary mode (e.g. images)

# Syntax

# f = open("demofile.txt")
# This will raise an error since the file does not exist at this moment

# The code above is the same as:
f = open("demofile.txt", "rt")
# This is no longer going to raise an error, since the file has
# since been created