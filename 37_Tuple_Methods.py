# Tuple Methods 
# Python has two built-in methods that you can use on tuples. 

# count() - Returns the number of times a specified value occurs in a tuple 

# Python Tuple count() Method
# Return the number of times the value 5 appears in the tuple: 
thistuple = (1, 3, 7, 8, 7, 9, 3, 2, 3, 4)
x = thistuple.count(3)
print(x)

# Definition and Usage 
# The count() method returns the number of times a specified value appears in the tuple. 

# Syntax 
# tuple.count(value)

# Parameter Values 
# Value = Required. The item to search for 


# index() - Searches the tuple for a specified value and returns the position of where it was found. 

# Python Tuple index() Method
# Search for the first occurence of the value 8, and return its position: 
thistuple = (1, 3, 5, 6, 7, 5, 3, 5, 2, 1)
x = thistuple.index(5)
print(x)

# Definition and Usage
# The index() method finds the first occurence of the specified value. 
# The index() method raises an exception if the value is not found. 

# Syntax 
# tuple.index(value)

# Parameter Values 
# value  -  Required. The item to search for 
