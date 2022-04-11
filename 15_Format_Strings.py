# Python - Format _ Strings 
# String Format 

# As we learned in the Python Variables chapter, we cannot combine strings and numbers linke this: 

# age = 36 
# txt = ("My name is Abhijeet, I am") + age
# print(txt)

# But we combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and paces them in the string where thr placeholders {} are:

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is Abhijeet, and I am {} Years old."
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
item_number = 9090
price = 90
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, item_number, price))