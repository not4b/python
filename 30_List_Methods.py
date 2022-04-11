# Python - List Methods 
# Python has a set of built-methods that you can use on lists.

# Method         Description 
# append()    -  Adds an element at the end of the list

# Python List append() Method

# add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# Definition and Usage
# The append() method appends an elecemnt to the end of the list. 

# Syntax 
# list.append(elmnt)

# Parameter Values 
# elmnt - Required. An element of any type (string, number, object etc.)

# More Examples
# Add a list to a list

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)


# clear()     -  Removes all the elements from the list

# Python List clear() Method
# Removes all elements from the fruits list: 

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# Definition and Usage 
# The clear() method removes all the elements from a list. 

# Syntax 
# list.clear()

# Parameter Values 
# No parameters 

# copy()      -  Returns a copy of the first list

# Python List copy() Method
# copy the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# Definition and Usage 
# The copy() method returns a copy of the specified list. 

# Syntax 
# list.copy()

# Parameter Values 
# No parameters

# count()     -  Returns the number of elements with the specified value

# Python List count() Method
# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# Definition and Usage
# The count() method returns the number of elements with the specified value. 

# Syntax
# list.count(value)

# Parameter Values 
# value - Required. Any type (string, number, list, tuple, etc.) The value to search for.

# More examples 
# Return the number times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# extend()    -  Add the elements of a list(or any iterable), to the end of the current list

# Python List extend() Method 
# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

# Definition and Usage 
# The extend() method adds the specified list elements (or any iterable) to the end of the current list. 

# Syntax 
# list.extend(iterable)

# Parameter Values 
# iterable - Required. Any iterable (list, set, tuple, etc.)

# More Examples
# Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)


# index()     -  Returns the index of the first element with the specified value 

# Python List index() Method 
# What is the position of the value "cherry":

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

# Definition and Usage 
# The index() method returns the position at the first occurrence of the specified value. 

# Syntax 
# list.index(elmnt)

# Parameter Values 
# elmnt - Required. Any type (String, number, list, etc.). The element to search for 

# More examples 
# What is the position of the value 32: 
fruits = [4, 55, 67, 16, 32]
x = fruits.index(32)
print(x)

# NOTE : The index() method only returns thew first occurence of the value 

# insert()    -  Adds an element at the specified postion

# Python List insert() Method

# Insert the value "orange" as the second element of the fruit list: 

fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, "orange")
print(fruits)

# Definition and Usage 
# The insert() method inserts the specified value at the specified position. 

# Syntax
# list.insert(pos, elmnt)

# Parameter Values 
# pos - Required. A number specifying in which position to insert the value
# elmnt - Required. An element of any type (string, number, object, etc. )

# pop()       -  Removes the element at the specified position 

# Python List pop() Method
# Remove the second element of the fruit list

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Definition and Usage 
# The pop() method removes the element at the specified position. 

# Syntax 
# list.pop(pos)

# Parameter Values 
# pos - Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item.

# More example 
# Return the removed element 

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop (1)
print(x)

# NOTE: The pop() method returns removed value.

# remove()    -  Removes the item with the specified value

# Python List remove() Method

# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# Definition and Usage 
# The remove() method removes the first occurance of the element with the specified value. 

# Syntax 
# list.remove(elmnt)

# Parameter Values 
# elmnt - Required. Any type (string, number, list etc.) The element you want to remove 


# reverse()   -  reverses the order of the list

# Python List reverse() Method 
# Reverse the order of the fruit list:

fruits =  ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Definition and usage 
# The reverse() method reverses the sorting order of elements. 

# Syntax 
# list.reverse()

# Parameter values 
# No parameter 

# sort()      -  Sorts the list

# Python List sort() Method
# Sort the list alphabetically

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# Definition and Usage 
# The sort() method sorts the list ascending by default. 
# You can also make a function to decide the sorting criteria(s).

# Syntax 
# list.sort(reverse= True|False, key=myFunc)

# Parameter Values 
# reverse - Optional. reverse = True will sort the list descending. Default is reverse = False 
# key     - Optional. A fuinction top specify the sorting criteria(s)

# More example 
# sort this list in the descending order: 

cars = ['Ford', 'BMW', 'volvo']
cars.sort(reverse=True)
print(cars)

# Sort the lsit by the length of the values: 
# A function that returns the length of the value: 
def myFunc(e):
    return len(e)
cars = ['Ford', 'Mercerdese', 'BMW', 'Volvo']
cars.sort(key=myFunc)
print(cars)

# Sort a list of dictionaries based on the "year" value of the dictionaries 

# A function that returns the 'year' value:
def myFunc(e):
    return e['year']
cars =  [
    {'car' : 'Ford', 'year': 2005}, 
    {'car' : 'Mercerdese', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car' : 'Volvo', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

# Sort the list by the length of the values and reversed:

# A function that returns the length of the value
def myFunc(e):
    return len(e)
cars = ['Ford', 'Mercedes', 'BMW', 'Volvo']
cars.sort(reverse=True, key=myFunc)
print(cars)

# NOTE : Python does not have built-in support for Arrays, but Python lists can be used instead.