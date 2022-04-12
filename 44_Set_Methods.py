# Set Methods 
# Python has a set of built-in methods that you can use on sets. 

# 01. add() - Adds an element to the set

# Python Set add() Method
# Add an element to the fruits set: 
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# Definition and Usage 
# The add() method adds an element to the set. 
# If the element already exists, the add() method does not add the element. 

# Syntax
# set.add(elmnt)

# Parameter Values 
# elmnt - Required. The element add to the set

# More Examples 
# Try to add an element that already exists: 
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

# 02. clear()  -    Removes an element to the set
# Python Set clear() Method
# Remove all elements from the fruits set: 
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# Definition and Usage 
# The clear() Method removes all elements in a set. 

# Syntax 
# set.clear() 

# Parameter Values
# No parameters

# 03. copy() - Returns a copy of the set
# Python Set copy() Method

# Copy the fruits set: 
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# Definition and Usage 
# The copy() method copies a set. 
# set.copy()

# Parameter Values
# No parameters 

# 04. difference()  - Returns a set containing the difference between two or more sets 
# Python Set difference() Method
# Return a set that contains the items that only exist in set x, and not in set y ; 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)
print(z)

# Definition and Usage
# The differnce() method returns a set that contains the difference between two sets. 
# Meaning: The returned set contains items that exist only in the first set, and not in both sets. 

# Syntax 
# set.difference(set)

# Parameter Values 
# set - Required. The set to check for differences in 

# More Examples
# Reverse the first example. Return a set that contains the items that only exist in set y , and not in set x : 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# 05. difference_update() - Removes the items in this set that are also include in another, specified set 
# Python Set difference_update() Method
# Remove the items that exist in both sets: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# Definition and Usage 
# The differnce_update() method removes the items that exist in both sets. 
# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set. 

# set.diifernce_update(set)

# Parameter Values 
# set -  Required. The set to check for differnces in 

# 06. discard() - Removes the specified item 
# Python Set discard() Method
# Remove "banana" from the set: 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# Definition and Usage 
# The discard() Method removes the specified item from the set. 
# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

# Syntax
# set.discard(value)

# Parameter Values
# value - Required. The item to search for, and remove

# 07. intersection() - Returns a set, that is intersection of two or more sets
# Python Set intersection() Method
# Return a set that contains the items that exist in both set x, and set y : 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Definition and usage 
# The intersection() method returns a set that conatains the similarity between two or more sets. 
# Meaning: The returned set contains ony items that exist in both sets, or in all sets if the comparison is done with more than two sets. 

# Syntax
# set.intersection(set1, set ... etc)

# Parameter values 
# set1 - Required. The set to search for equal items in
# set2 - Optimal. The other set to seach for equal items in. you can comapare as many sets as you like. Seperate the sets with a comma. 

# More Examples
# Compare 3 sets, and return a set with item that is present in all 3 sets: 

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

# 08_intersection_update() - Removes the items in this set that are not present in other, specified set(s)

# Python Set intersection_update() Method 
# Remove the items that is not present in both x and y : 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Definition and Usage 
# The intersection_update() method removes the items that is not present in both (or in all sets if the comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() removes the unwanted items the original set. 

# Syntax 
# set.intersection_update(set1, set2, ... etc)

# Parameter Values 
# set1 - Required. The set to reach for equal items in 
# set2 - Optional. The other set to search for equal in. You can compare as many sets you like. Separate the sets with a comma. 

# More Examples 
# Compare 3 sets, and return a set with items that is present in all 3 sets: 

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)
print(x)

# 09. isdisjoint() - Returns whether two sets have a intersection or not. 
# Python Set isdisjoint() Method

# Return True if no items in set x is present in set y : 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# Definition and Usage 
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

# Syntax
# set.isdisjoint(set)

# Parameter Values 
# set - Required. The set to search for equal items in 

# More examples
# What if no items are present in both sets? 
# Return False if one or more items are present in both sets: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

# 10. issubset() - Returns whether another set contains this set or not
# Python Set issubset() Method
# Return True if all items in set x are present in set y:
x = {"a","b", "c"} 
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Definition and Usage 
# The issubset() method returns True if all items in the set exist in the specified set, otherwise it returns False. 

# Syntax
# set.issubset(set)

# Parameter Values
# set - Required. The set to search for eqaul items in 

# More examples 

# What id not all items are present in the specified set? 
# Returns False if not all items in set x are present in set y: 
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

# 11. issuperset() - Returns whether this set contains this set or not
# Python Set issuperset() Method
# Return True if all items set y are present in set x :

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)

# Definition and Usage 
# The issuperset() method returns True if all items in the specified set exist in the original set, otherwise it returns False. 

# Syntax 
# set.issuperset(set)

# Parameter Values 
# set - Required. The set to search for equal items in 

# More Examples
# What if not all items are present in the specified set? 
# Return False if not all items in set y are present in set x: 

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# 12. pop() - Removes an element from this set contains another set or not
# Python Set pop() Method
# Remove a random item from the set: 
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# Definition and Usage 
# The pop() method removes a random item from the set. 
# This method returns the removed item. 

# Syntax
# set.pop()

# Parameter Values 
# No parameter values. 

# More Examples 
# Return the removed element: 
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)
# NOTE : The pop() method returns removed value. 

# 13. remove() - Removes the specified element 
# Python Set remove() Method
# Remove "banana" from the set: 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# Definition and Usage 
# The remove() method removes the specified element from the set. 
# This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not. 

# Syntax 
# set.remove(item)

# Parameter Values 
# item - Required. The item to search for, and remove 

# 14. symmetric_difference_update() - inserts the symmetric differences from this set and another
 
# Python Set symmetric_difference_update() Method 

# Remove the items that are present in both sets, AND insert the items that is not present in both sets: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

# Definition and USage 
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets and inseting thr other items.

# Syntax 
# set.symmetric_difference_updaṭe(set)
# Parameter Values 
# set - Required. THe set to check for matches in 

# 15. symmetric_difference() - Returns a set with the symmetric differences of two sets. 
# Python Set symmetric_difference() Method
# Return a set that contains all items from both sets, except that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "micrsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Definition and Usage 
# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are prensent in both sets 
# Meaning: The returned set contains a mix of items that are not present in both sets. 

# Syntax 
# set.symmetric_difference(set)

# Parameter Values 
# set - Required. The set to check for matches in 

# 16. union() - Return a set containing the union of sets
# Python Set union() Method
# Return a set that contains all items from both sets, duplicates are excluded: 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z - x.union(y)
print(z)

# Definition and Usage 
# The union() method returns a set that contains all items from the original set, and all items from the specified set(s)
# You can specify as many sets you want, separated by commas. 
#  It does not have to be a set, it can be any iterable object. 
# If an item is present is more than one set, the result will contain only one appearance of this item. 

# Syntax
# set.union(set1, set2...)

# Parameter Values 
# set1 - Required. The iterable to unify with
# set2 - Optional. The other iterable to unify with.You can compare as many iterables as you like. separate each iterable with a comma. 

# More Examples 
# Unify more than 2 sets: 
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)

# 17. update() - Update the set with another set, or any other iterable 
# Python Set update() Method
# Insert the items from set y into set x: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# Definition and Usage 
# THe update() method updates the curent set, by adding items from another set( or any other iterable ). 
# If an item is present in both sets, only one appearance of this item will be present in the updated set. 

# Syntax 
# set.update(set)

# Parameter Values
# set - Requied. The iterable insert into the current set
