# Python Sets 
import this


myset = {"apple", "banana", "cherry"}

# Set 
# Sets are used to store multiple items in a single variable. 
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. 
# A set is a collection is unordered, unchangeable*, and unindexed. 

# NOTE: Set items are unchangeable, but you can remove items and add new items. 

# Sets are written with curly brackets. 

# Create a Set: 
thisset = {"apple", "banana", "cherry"}
print(thisset)

# NOTE: Sets are unordered, so you cannot be sure in which order the items will appear. 

# Set Items 
# Set items are unordered, unchangeable, and do not allow duplicate values. 

# Unordered 

# Unordered means that the items in a set do not have a defined order. 
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable 
# Set items are unchangeable, meaning that we cannot change the items after the set has been created. 

# Once a set is created, you cannot change its items, but you can remove items and items and add new items. 

# Duplicates Not Allowed 
# Sets cannot have two items with the same value. 
# Duplicate values will be ignored: 

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Get the length of a set 
# To determine how many items a set has, use the len() function. 
# Get the number of items in a set: 
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types 
# Set items can be any data type: 

# String, int and boolean data types: 
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 4, 9, 7, 6}
set3 = {True, False, False}

# A set can contain different data types: 

# A set with strings, integers and boolean values: 
set1 = {"abc", 45, True, 40, "male"}
print(set1)

# type()
# From Python's perspective, sets are defined as objects with the data 'set': 
# <class 'set'>

# What is the data type of a set? 
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor 
# It is also possible to use the set() construct to make a set. 

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Pythonh Collections (Arrays)
# There are four collection data types in Python programming language:

# List is a collection of which is ordered and changeable. Allows duplicate members. 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchnageable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members. 

# *Set items are unchangeable, but you can remove items and add new items. 
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. 

# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficienct or security. 

 