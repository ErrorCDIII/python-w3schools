# Escape Character
# An escape character is a backslash \ followed by the character you want to insert.

# This will generate an error -> double quotes inside double quotes
# txt = "We are the so-called "Vikings" from the north."

# This will prevent the previous error
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters
# Code  Result              Example
# \´    Single Quote        txt = 'It\'s alright.'
# \\    Backslash           txt = "This will insert one \\."
# \n    New Line            txt = "This will print a \n new line"
# \r    Carriage Return     txt = "Hell\rWorld!"
    # This example will print: "World!"
# \t    Tab                 txt = "Hello\tWorld!"
# \b    Backspace           txt = "Hello\bWorld!"
    #This example will print: "HellWorld!"
# \f    Form Feed  
    # This character is obsolete and works nowadays as an invisible seperator
# \ooo  Octal Value         txt = "\110\145\154\154\157"
    # This example will print: "Hello"
# \xhh  Hexadecimal Value   txt = "\x48\x65\x6c\x6c\x6f"
    # This example will print: "Hello"