print(10 + 5)

# Python divides the operators in the following groups:

#     Arithmetic operators
#     Assignment operators
#     Comparison operators
#     Logical operators
#     Identity operators
#     Membership operators
#     Bitwise operators

# Python Arithmetic Operators

# Operator    Name            Example
# +           Addition        x + y       
# -           Subtraction     x - y
# *           Multiplication  x * y
# /           Division        x / y
# %           Modulus         x % y
# **          Exponentiation  x ** y
# //          Floor division  x // y

# Python Assignment Operators

# Operator    Example         Same as
# =           x = 5           x = 5
# +=          x += 3          x = x + 3
# -=          x -= 3          x = x - 3
# *=          x *= 3          x = x * 3
# /=          x /= 3          x = x / 3
# %=          x %= 3          x = x % 3
# //=         x //= 3         x = x // 3
# **=         x **= 3         x = x ** 3
# &=          x &= 3          x = x & 3
# |=          x |= 3          x = x | 3
# ^=          x ^= 3          x = x ^ 3
# >>=         x >>= 3         x = x >> 3
# <<=         x <<= 3         x = x << 3
# :=          print(x := 3)   x = 3
#                             print(x)

# Python Comparison Operators

# Operator    Name                        Example
# ==          Equal                       x == y
# !=          Not equal                   x != y
# >           Greater than                x > y
# <           Less than                   x < y
# >=          Greater than or equal to    x >= y
# <=          Less than or equal to       x <= y

# Python Logical Operators

# Operator    Description                         Example
# and         Returns True if both are true       x < 5 and x < 10
# or          Returns True at least one is true   x < 5 or x < 4
# not         Reverses the result                 not(x < 5 and x < 10)

# Python Identity Operators

# Operator    Description                                     Example
# is          Returns True if both are the same object        x is y
# is not``    Returns True if both are not the same object    x is not y

# Python Membership Operators

# Operator    Description                                                                         Example
# in          Returns True if a sequence with the specified value is present in the object        x in y
# not in      Returns True if a sequence with the specified value is not present in the object    x not in y

# Python Bitwise Operators
# Operator    Name                    Description                                                                                                 Example
# &           AND                     Sets each bit to 1 if both bits are 1                                                                       x & y
# |           OR                      Sets each bit to 1 if one of two bits is 1                                                                  x | y
# ^           XOR                     Sets each bit to 1 if only one of two bits is 1                                                             x ^ y
# ~           NOT                     Inverts all the bits                                                                                        ~x
# <<          Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off                            x << 2
# >>          Signed right shift      Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off     x >> 2

print()

# Operator Precedence

# Parentheses has the highest precedence
print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +
print(100 + 5 * 3)

# Operator                                Description
# ()                                      Parentheses
# **                                      Exponentiation
# +x -x ~x                                Unary plus, unary minus, bitwise NOT
# * / // %                                Multiplication, division, floor division, modulus
# + -                                     Addition and subtraction
# << >>                                   Bitwise left and right shifts
# &                                       Bitwise AND
# ^                                       Bitwise XOR
# |                                       Bitwise OR
# == != > >= < <= is is not in not in     Comparisons, identity, membership
# not                                     Logical NOT
# and                                     Logical AND
# or                                      Logical OR

# With same precedence operators the evaluation is performed left to right
print(5 + 4 - 7 + 3)