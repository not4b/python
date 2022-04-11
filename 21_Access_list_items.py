# Python - Access List Items 
# List items are indexed and you can access them by referriong to the index number:

# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

# NOTE: The first item has index 0. 

# Negative Indexing 
# Negative indexing means start from the end 
# -1 refers to the last item, -2 refers to the second last item etc.

# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes 
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with specified items. 

# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# NOTE: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.
# By leaving out the start value, the range will start at the first item:

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# This will return the items from index 0 to index 2.
# Remember that index 0 is the first item, and index 4 is the fifth item 
# Remember that the item in index 4 is NOT included

# By leaving out the end value, the range will go on to the end of the list:

# this example returns the items from "cherry" to the end: 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes 
# Specify negative indexes if you want to start the search from the end of the list:

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exist 
# To determine if a specified item is present in a list use the in keyword:

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
    