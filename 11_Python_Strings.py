# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello"

# You can display a string literal with the print() function:

print("Hello")
print('Hello')

# Assign String to a Variable 

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiple string to a variable by using three quotes:

# You can use three double quotes:
a = """Imagination is more powerfull than knowledge because knowledge is limited whereas imagination encircles the universe_____ALBERT_EINSTINE"""
print(a)

# Or three single quotes: 
a = '''Imagination is more powerfull 
than knowledge because knowledge 
is limited whereas imagination encircles 
the universe_____ALBERT_EINSTINE'''
print(a)

# NOTE: in the result, the line breaks are inserted at the same position of code.

# Strings are Arrays 
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

#Strings are Arrays 

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1 

# Square backets can be used to access elements of string.

# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

# Looping Through a String 

# Since strings are arrays, we can loop through the charcaters in a string, with a for loop.

# Loop through the letters in the word "banana":

for x in "banana":
    print(x)

# String Length
# To get the length of a string, use the len() function.

# the len() functions the length of a string:

a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement: 
# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the Keyword not in.

# Check if "expensive" is NOT present present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement 

# Print only if "expensive" is NOT present:

text = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    

