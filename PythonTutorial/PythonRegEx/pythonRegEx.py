# Python RegEx

# A RegEx, or Regular Expression, is a sequence of 
# characters that forms a search pattern

# RegEx can be used to check if a string contains the specified
# search pattern

# RegEx Module

import re

# RegEx in Python

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 

print(x)

# RegEx Functions

# Function    Description
# findall     Returns a list containing all matches
# search      Returns the Match object if there is a match anywhere in the string
# split       Returns a list where the string has been split at each match
# sub         Replaces one or many matches with a string

# Metacharacters

# Character   Description                     Example
# []          A set of characters             "[a-m]"
# \           Signals a special sequence      "\d"
#             (can also be used to escape     "he..o"
#             special characters)
# .           Any character (except newline)  "^ĥello"
# ^           Starts with                     "^ĥello"
# $           Ends with                       "planet$"
# *           Zero or more occurences         "he.*o"
# ?           One or more occurences          "he.?o"
# {}          Exactly the specified number    "he.{2}o"
#             of occurences
# |           Either or                       "falls|stays"
# ()          Capture the group

# Flags

# Flag            Shorthand   Description
# re.ASCII        re.A        Returns only ASCII matches
# re.DEBUG                    Returns debuf information
# re.DOTALL       re.S        Makes the . character match all characters (including newline character)
# re.IGNORECASE   re.I        Case-insensitive matching
# re.MULTILINE    re.M        Returns only matches at the begginning of each line
# re.NOFLAG                   Specifies that no flag is set for this patter
# re.UNICODE      re.U        Returns UNICODE matches. This is the default
# re.VERBOSE      re.X        Allows whitespaces and comments inside patterns.
#                             Makes the pattern more readable

# Special Sequences

# A special sequence is a \ folowed by one of the characters in the list below

# Character   Description                             Example
# \A          Returns a match if the specified        "\AThe"
#             characters are at the beginning         r"\bain"  
#             of the string                           r"ain\b"
# \b          Returns a match where the specified     
#             characters are at the beginning or
#             end of a word
# \B          Returns a match where the specified    r"\Bain"
#             characters are present, but NOT at     r"ain\B"
#             the beginning, or end of a word
# \d          Retrurns a match where the string     "\d"
#             contains digits
# \D          Returns a match where the string      "\D"
#             DOES NOT contain digits
# \s          Returns a match where the string      "\s"
#             contains white spaces
# \S          Returns a matcah where the string     "\S"
#             DOES NOT contain white spaces
# \w          Returns a match where the string      "\w"
#             contains any word characters
# \W          Returns a match where the string      "\W"
#             DOES NOT contain any word characters
# \Z          Returns a match if the specified      "Spain\Z"
#             characters are at the end of
#             the string

# Sets

# Set         Description
# [arn]       Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]       Returns a match for any lower case character, alphabetically between a and n
# [^arn]      Returns a match for any character EXCEPT a, r, and n
# [0123]      Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]       Returns a match for any digit between 0 and 9
# [0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]    Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]         In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

# The findall() Function
# The findall() function returns a list containing all macthes

import re

print()

txt = "The rain in Spain"
x = re.findall("ai", txt)
y = re.findall("Portugal", txt)
print(x)
print(y)

# The search() Function
# The search() function searches the string for a match for 
# a match, and returns a Match object if there is a match

# If there is more than one match, only the first occurrence
# of the match will be returned

import re

print()

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned

# The split() Function
# The split() function returns a list where the string has been
# split at eatch match

import re

print()

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# You can control the number of occurrences by specifying the 
# maxsplit parameter

import re

print()

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice

import re

print()

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements with the count parameter

import re

print()

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object
# A Match Object is an object containing information about the 
# search and the result

# Note: if there is no match, the value None will be returned
# instead of a Match Object

import re

print()

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

# The Match Object has properties and methods used to retrieve 
# information about the search, and the result
#   .span() -> returns a tuple containing the start-, and end 
# positions of the match
#   .string() -> returns the string passed into the function
#   .group() -> returns part of the string where there was a match

import re

print()

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

print()

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print()

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())