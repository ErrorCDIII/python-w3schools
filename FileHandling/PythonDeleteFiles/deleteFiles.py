# Delete Files

# To delete a file, you must import the OS module, and run it's
# os.remove() function

import os

# os.remove("demofile.txt")
# Note: will raise an error since the files does not exist

# Check if File Exists

# To avoid getting an error, you might want to check if the file 
# exists before you try to delete it

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist.")

# Delete Folder

# To delete an entire folder, use the os.rmdir() method:

import os

os.rmdir("myfolder")
# Note: this will raise an error since the folder doesn't exist
# Note: you can only remove empty folders