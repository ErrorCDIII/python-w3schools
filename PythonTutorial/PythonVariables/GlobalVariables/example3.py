# The gobal keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myFunc():
    global x
    x = "fantastic"

myFunc()

print("Python is " + x)
# Even though x was created inside a function, since it's global, it's scope is also globlal