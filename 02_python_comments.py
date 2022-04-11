# Comments can be used to explain Python code.
# Comments can be used to make code more readable.
# Comments can be used to prevent execuition when testing code.

# This is a Comment
print("Hello World")

# Comments can be placed at the end of line, and python will ignore rest of the line:

print("Hello, World") # This is a comment 

# A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:

# print("Hello World")
print("Cheers, Mate!")

# Multi line comments 
# Python does not really have a syntax for multi line comments/
# to add a multiline comment you could insert # for each line:

# This is a comment 
#written
#in more than just one line
print("Hello World")

# or not quite as intended, you can use a multiline string.

# Since Python will ignore string literals that are not assigned to a variable, you can add multine string(truple quotes) in your code, and place you comment inside it:

"""
This is a comment 
written in 
more than just one line 
"""
print("Hello, World!")

# as long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment. 
