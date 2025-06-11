# PIP

# PIP is package manager for Python

# What's a Package?

# A package contains all the files you need for a module
# Modules in Python are code libraries you can include in your project

# Download a Package
# Example_ download a package named "camelcase"
# pip install camelcase

# Using a Package
# Once the package is installed, it's ready to use.
# Just import it as usual

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# Remove Packages

# Use the uninstall command
# pip uninstall camelcase

# List Packages

# Use the list command
# pip list
