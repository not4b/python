# Python - Escape Characters 
# Escape Characters 

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert. 
# An example of an illegal character is a double quote inside a string is surrounded by double quotes. 

# You will get an error if you use double quotes inside a stringt that is surrounded by double quotes: 

# txt = "We are the so-called "Vikings" from the north."

# The escape character allows you to use double quotes when you normally would not be allowed: 
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

pr = "I am \"Abhijeet\" Kumar."
print(pr)

# Escape Charcters 
# Other escape characters used in Python:

# \'  Single Quote
# \\ Backslash
# \n New Line 
# \r Carriage Return 
# \t Tab
# \b Backspace
# \f Form Feed
# \ooo Octal Value
# \xhh Hex value
