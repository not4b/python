# Buil-in Data Types

# In programming, data type is an important concept.
# variables can store data of different types, and different types can to different things. 
# Python has the following data types built-in by default, in these categories:

# Text Type: str
# Numeric Type: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Types: dict
# Set Types: set, frozenset
# Boolean Type: bool 
# Binary Types: bytes, bytearray, memoryview

# Getting the Data Type 
# You can get the data type of any by using the type() function:

# Print the data type of variable x:
x = 5
print(type(x))

# Setting the Data Type 
# In Python, the data type is set when you assign a value to a variable: 

# str 
x = "Hello World" 

#int
x = 20

# float
x = 20.5

# complex
x = 1j

# list
x = ["apple", "banana", "cherry"]

#tuple
x = ("apple", "orange", "cherry")

#range
x = range(6)

#dict
x = {"name" : "abhijeet", "age" : 19}

#set
x = {"apple", "banana", "cherry"}

#frozenset
x = frozenset({"apple", "banana", "cherry"})

#bool
x = True

#bytes
x = b"Hello"

#bytearray
x = bytearray(5)

#memoryview
x = memoryview(bytes(5))

# Setting the Specific Data Type 
# If you want to specify the data type, you can use the following constructor functions:

# str 
x = str("Hello World") 

#int
x = int(20)

# float
x = float(20.5)

# complex
x = complex(1j)

# list
x = list(("apple", "banana", "cherry"))

#tuple
x = tuple(("apple", "orange", "cherry"))

#range
x = range(6)

#dict
x = dict(name="abhijeet", age = 19)

#set
x = set(("apple", "banana", "cherry"))

#frozenset
x = frozenset(("apple", "banana", "cherry"))

#bool
x = bool(5)

#bytes
x = bytes(5)

#bytearray
x = bytearray(5)

#memoryview
x = memoryview(bytes(5))

