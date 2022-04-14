# Python - Access Dictionary Items 
# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Get the value of the "model" key: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
 }
x = thisdict["model"]
print(x)

# There is also a method called get() that will give the same result: 
# Get the value of the "model" Key:
x = thisdict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary. 

# Get a list of the keys: 
x = thisdict.keys()
print(x)

#The list of the keys is a view of the dictionary, meaning that any charges done to the dictionary will be reflected in the keys list. 

# Add a new item to the original dictionary, and see that the keys list gets updated as well: 

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x) # before the change
car["color"] = "white"
print(x) # after the change
print(car)

# Get Values 
# The values() method will return a list of all values in the dictionary.

# Get a list of the values:
x = thisdict.values()
print(x)

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list. 

# Make a change in the original dictionary, and see that the values list gets updated as well: 


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) # Before the change 
car["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the values list gets updated as well: 


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) # Before the chnage
car["color"] = "red"
print(x) # after the change 

# Get Items 
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs 
x = thisdict.items()
print(x)

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list. 

# Make a change in the original dictionary, and see that the items list gets updated as well: 


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) # before the chnage
car["year"] = 2020
print(x) # after the change

# Add a new item to the original dictionary, and see that the items list gets updated as well: 

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) # before the change
car["color"] = "red"
print(x) # after the change 

# Check if key Exists 
# To determine if a specified key is present in a dictionary use the in keyword: 

# Check if "model" is present in the dictionary: 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang", 
    "year" : 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("No, 'model' is not one of the keys in the thisdict dictionary")