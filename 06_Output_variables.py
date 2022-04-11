# The python print() function is often used to output variables. 
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, sparated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# NOTICE the space character after "Python " and "is ", without them the result would be "Pythonisawesome"

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# x = 5
# y = "abhi"
# print(x+y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different datas types:

x = 5
y = "Abhi"
print(x, y)
