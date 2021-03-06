# Python Dictionaries 

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

# Dictionary
# Dictionaries are used to store data values in key : value pairs.
# A  dictionary is a collection which is ordered*, changeable and not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. 

# Dictionaries are written with brackets, and have keys and value: 
# create and print a dictionary: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
 }
print(thisdict)

# Dictionary Items 
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key: value pairs, and can be referred to by using the key name. 

# Print the "brand" value of the dictionary: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
 }
print(thisdict["brand"])

# Ordered or Unordered? 

# As Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. 

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not chnage. 

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index. 

# Changeable 
# Dictionaries are changeable, meaning that we can chnage, add or remove items after the dictionay has been created. 

# Duplicates Not Allowed 
# Dictionaries cannot have two items with the same key: 
# Duplicate values will overwrite existing values: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964", 
    "year":  "2020"
 }
print(thisdict)

# Dictionary Length
# To determine how many items a dictionary has, use the len() function: 

# Print the number of items in the dictionary: 
print(len(thisdict))

# Dictionary Items - Data Types 
# The values in dictionary items can be of any data type: 
# string, int, boolean, and list data types: 
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : "1964",
    "colors": ["red", "white", "blue"]
 }
print(thisdict)

# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dic':
# <class 'dict'>

# Print the data type of a dictionary: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
 }
print(type(thisdict))

# Python Collections (Arrays)
# There are four collection data types in the Python programming language: 

# List is a collection which is ordered and changeable. Allows duplicate members. 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. 
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like. 
# ** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set culd mean retention of meaning, and, it could mean an increase in efficiency or security. 