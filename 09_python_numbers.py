# Python Numbers
# There are three numeric in Python 

# int
# float
# complex

# Variables of numeric types are created when you assign a value to them:

x = 1   # int
y = 2.8 # float
z = 1j  # complex

# to verify the type of any object in Python, use the type() function:

print(type(x))
print(type(y))
print(type(z))

# Int
# Int or integer, is a whole number, posiutive or negative, without decimals, of ultimate length.

# Integers 

x = 1
y = 8098980898079879807
z = -787878

print(type(x))
print(type(y))
print(type(z))

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Floats

x = 2.3
y = 1.0
z = -89.2

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

# Floats:

x = 36e2
y = 123E2
z = -89.8e100

print (z)
print(type(x))
print(type(y))
print(type(z))

# Complex
# complex numbers are written with a "j" as the imaginary part:

x = 2+4j
y = 8j
z = -2j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

# You can convert from one type another with the int(), float(), and complex() methods:

# Convert from one type to another: 
x = 1 # int
y = 2.9 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# NOTE: You cannot convert complex numbers into another number type.

# Random Number 
# Python does not have a random() function to make number, but python has a built-in- module called rando, that can be used to make random numbers:

# Import the random module, and display a random between 1 and 9:
import random
print (random.randrange(1, 6 ))


