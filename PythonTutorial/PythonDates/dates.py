# Python Datetime

# Python Dates

# A date in Python is not a data type of it's own, but we
# can import a module named datetime to work with dates
# as date objects.

# Example: import the datetime module and display the
# current date
import datetime

x = datetime.datetime.now()
print(x)

# Date Output

# The date contains year, moth, day, hour, minute, second,
# and microsecond

print()

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects

# To create a date, we can use the datetime() class 
# constructor of the datetime module

# The datetime() class requires three parameters to 
# create a dtae: year, moth, day

import datetime

print()

x = datetime.datetime(2020, 5, 17)

print(x)

# The datetime() class also takes parameters for time
# and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0
# (None for timezone)

# The strftime() Method

# The datetime object has a method for formatting date
# objects into readable strings

# The method is called strftime(), and takes one parameter
# format, to specify the format of the returned string

# Example: display the name of the month:
import datetime

print()

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# A reference of all the legal format codes:
# Directive   Description                 Example
# %a          Weekday, short version      Wed
# %A          Weekday, full version       Wednesday
# %w          Weekday as a number         3
#             0-6, 0 is Sunday
# %d          Day of the month 01-31      31
# %b          Month name, short version   Dec
# %B          Month name, full version    December
# %m          Month as a number 01-12     12
# %y          Year, short version,        18
#             without century
# &Y          Year, full version          2018
# %H          Hour 00-23                  17
# %I          Hour 00-12                  05
# %p          AM/PM                       PM
# %M          Minute 00-59                41
# %S          Second 00-59                08
# %f          Microsecond                 548513
#             000000-999999
# %z          UTC offset                  +0100
# %Z          Timezone                    CST
# %j          Day number of year          365
#             001-366
# %U          Week number of year,        52
#             Sunday as the first day
#             of week, 00-53
# %W          Week number of year,        52
#             Monday as the first day
#             of week, 00-53
# %c          Local version of date       Mon Dec 31 17:41:00
#             and time
# %C          Century                     20
# %x          Local version of date       12/31/18
# %X          Local version of time       17:41:00
# %%          A % character               %
# %G          ISO 8601 year               2018
# %u          ISO 8601 weekday (1-7)      1
# %V          ISO 8601 weeknumber         01
#             (01-53)
