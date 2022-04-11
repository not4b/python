# Variables are containers for storing data values 
# python has no command for declaring a variable
# A variable is created the moment you first assign value to it.

x = 5 
y = "Abhi"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4   # x is of type int
x = "Sally" # x is now a type of str
print(x) 

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x, y, z)

# get the type
# You can get the data type of a variable with type() function.

x = 5
y = "Abhi"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

x = "abhi"
# is the same as 
x = 'abhi'
print(x)

# case - Sensitive
# Variable names are case-sensitive

a = 4
A = "sally"
# A will not overwrite a 
print(a)
print(A)

