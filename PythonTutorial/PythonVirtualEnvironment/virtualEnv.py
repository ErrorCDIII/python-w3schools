# Virtual Environment

# What is a Virtual Environment?

# A virtual environment is an isolated environment on your 
# computer, whare tou can run and test Python projects.

# It allows you to manage project-specific dependencies without
# interfering with other projects or the original Python installation

# Each container:
#   Has it's own Python interpreter
#   Has it's own set of installed packages
#   Is isolated from other virtual enviroments
#   Can have different versions of the same package

# Using virtual environments is important because:
#   It prevents package version conflicts between projects
#   Makes projects more portable and reproducible
#   Keeps your system Python installation clean
#   Allows testing with different Python versions

# Creating a Virtual Environment

# Python has the built-in venv module for creating virtual environments

# To create a virtual environment on your computer, open the
# command prompt, and navigate to the folder where you want to 
# create your project, then type:

# Example: 
# python3 -m venv myfirstproject

# This will set up a virtual environment, and create a fodler 
# named "myfirstproject" with subfolders and files

# Activate Virtual Environment
# source myfirstproject/bin/activate
# After activation the prompt will change to indicate it

# Install Packages

# Once your virtual environment is activated, you can install
# packages in it, using pip

# We will install a package called 'cowsay'

# Example: install 'cowsay' in the virtual environment
# pip install cowsay

# Using a Package

# Not that the 'cowsay' module is intalled in your virtual 
# environment, lets use it

# Create a file called test.py.
# You can place it wherever you want

# Deactivate Virtual Environment

# Inside the virtual environment terminal

# deactivate
# The terminal you go back to it's regular state

# If you try to execute test.py outside of the virtual environment,
# you will get an error because 'cowsay' is missing.
# It was only installed in the virtual environment

# Note: the virtual environment myfirstproject still exists, it is
# just not activated. If you activate it again, you can execute the
# test.py file

# Delete Virtual Environment

# Another nice thing about working with virtual environments it
# that when you, for some reason want to delete it, there are no
# other projects depending on it, and only modules and files in
# the specified virtual environment are deleted

# To delete a virtual environment, you can simply delete the folder