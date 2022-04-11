# String Methods 
# Python has a set of built-in-methods that you canb use on strings. 

# NOTE : All string methods will return new values. They do not change the original string 

# capitalize() - Converts the first Character to upper case 
# casefold()   - Converts strings into lower case 
# center()     - Returns a centered string 
# count()      - Returns the number of times a specified value occurs in a string
# endcode()    - Returns an endcode version of the string 
# endswith()   - Returns true if the string ends with the specified value 
# expandtabs() - Sets the tab size of the strinf 
# find()       - Searches the string for a specified value and returns the position of where it was found 
# format()     - Formats specified values in a string 
# format_map() - Formats specified values in a string
# index()      - Searches the string for a specified value and returns the position of where it was found
# isalnum()    - Returns True if all characters in a string are alphanumeric 
# isalpha()    - Returns True if all characters in a string are in the alphabet 
# isdecimal()  - Returns True if all characters in a string are decimals 
# isdigit()    - Returns True if all characters in a string are digits 
# isidentifier() - Returns True if the string is an identifier
# islower()      - Returns True if all characters in a string are lowercase
# isnumeric()    - Returns True if all characters in a string are numeric
# isprintable()  - Returns True if all charcaters in a string are printable
# isspace()      - Returns True if all characters in a string are whitespaces
# istitle()      - Returns True if the string follows the rules of a title
# isupper()      - Returns True if all characters in the string are upper case
# join()         - Join the elements of an iterable to the end of the string 
# ljust()        - Returns a left justified version of the string 
# lower()        - Converts a string into lower case
# lstrip()       - Returns a left trim version of the string
# maketrans()    - Returns a translation table to be used in translations
# partition()    - Returns a translation table to be used in translation 
# replace()      - Returns a string where where a specified value is replaced with a specified value
# rfind()        - Searches the string for a specified value and returns the last position of where it was found 
# rindex()       - Searches the string for a specified value and returns the last position of where it was found 
# rjust()        - Returns a right justified version of the string 
# rpartition()   - Returns a tuple where the string is parted into three parts
# rsplit()       - Splits the string at the specified separator, and returns a list
# rstrip()       - Returns a right trim version of the string 
# split()        - Splits the string at line breaks and returns a list 
# startswith()   - Returns true if the string starts with the specified value 
# strip()        - Returns the trimmed version of the string 
# swapcase()     - Swaps cases, lower case becomes upper case and vice versa 
# title()        - Converts the first character of each word to upper case
# translate()    - Returns a translated string
# upper()        - Converts a string into upper case
# zfill()        - Fills the string with a specified number of 0 values at the beginning 


# Python Strings Exercise :- 
# 1. Use the len method to print the length of the string. 
x = "Hello World"
print(len(x))

# 2. Get the first charcter of the string txt.
txt = "Hello World"
x = txt[0]
print(x)

# 3. Get the characters from index 2 to index 4 (llo)
txt = "Hello World"
x = txt[2:5]
print(x)

# 4. Return the string without any whitespace at the beginning or the end. 
txt = " Hello World "
x = txt.strip()
print(x)

# 5. Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
print(txt)

# 6. Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
print(txt)

# 7. Replace the character H with a J. 
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)

# 8. Insert the correct syntax to add a placeholder for the age parameter.
age = 19
txt = "My name is Abhijeet, and I am {}"
print(txt.format(age))
