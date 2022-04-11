# Python Operators 

# Operators are used to perform operations on variables and values. 
# In the example below, we use the + Operator to add together two values 

from re import X


print(10 + 2)

# Python divides the operators in the following groups: 

# Aritmetic operators
# Assignment operators
# Comparison operators 
# Logical operators 
# Identity operators 
# Membership operators 
# Bitwise operators 

# Python Arithmatic Operators 
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator    Name             Example
#    +        Addition           x+y     
x = 5
y = 3

print(x+y)
#    -        Subtraction        x-y
x = 5
y = 3

print(x-y)
#    *        Multiplication     x*y
x = 5
y = 3

print(x*y)
#    /        Division           x/y
x = 5
y = 3

print(x/y)
#    %        Modulus            x%y
x = 5
y = 3

print(x%y)
#    **       Exponentiation     x**y
x = 5
y = 3

print(x**y)
#    //       Floor division     x // y
x = 5
y = 3

print(x//y)

# Python Assignment Operators 
# Assignment operators are used to assign values to variables:

# Operator         Example          Same As
#  =               x = 5             x = 5
x = 5
print(x)

#  +=              x += 3            x = x + 3
x = 5
x += 3
print(x)

#  -=              x -= 2            x = x - 3
x = 5
x -= 3
print(x)

#  *=              x *= 3            x = x * 3
x = 5
x *= 3
print(x)

#  /=              x/=3              x = x / 3
x = 6
x /= 3
print(x)

#  %=              x %= 3            x = x % 3
x = 5
x %= 3
print(x)

#  //=             x //= 3           x = x // 3
x = 5
x //= 3
print(x)

# **=              x **= 3           x = x ** 3
x = 4
x **= 3
print(x)

#  &=              x &= 3            x = x & 3
x = 5
x &= 3
print(x)

#  |=               x |= 3           x = x | 3
x = 5
x |= 3
print(x)

#  ^=               x ^= 3           x = x ^ 3
x = 5
x ^= 3
print(x)

#  >>=             x >>= 3           x = x >> 3
x = 5
x >>= 3
print(x)

# <<=             x <<= 3            x = x << 3
x = 5
x <<= 3
print(x)

# Python Comparison Operators 

# Comparison operators are used to compare two values :

# Operator         Name                   Example
#   ==            Equal                  x == y 
x = 5 
y = 3

print(x == y)
# return False because 5 is not equal to 3 

#   !=            Not equal              x != y
x = 5
y = 3

print(x != y)
# returns True because 5 is not equal to 3

#    >             Greater than          x > y 
x = 5
y = 3

print(x > y)
# returns True because 5 is greater than 3

#    <            Less than             x < y
x = 5 
y = 3

print(x < y)
# return False because 5 is not les than 3 

#    >=           Greater than or equal to    x >= y

x = 5 
y = 3

print(x >= y)
# returns True because five is greater, or equal, to 3

#    <=            Less than or equal to        x <= y

x = 5
y = 3 

print(x <= y)
# returns False because 5 is neither less than or equal to 3  

# Python Logical Operators 
# Logical operators are used to combine conditional statements: 
# and - Returns True if both statements are true   x < 5 and x < 10

x = 5 
print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

# or - Returns True if one of the statements is true        x < 5 ort x < 4

x = 5

print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# not - Reserve the result, returns False if the  not(x < 5 and x < 10) result is true

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reserve the result 

# Python Identity Operators 
# Identity Operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is - Returns True if both variables are the same object   x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print (x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content 
print(x == y)
# to demonstrate the difference between "is" and "==" : this comparison returns True because x is equal to y 


# is not  - Returns True if both variables are not the same object   - x is not y 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print(x is not z)
# returns False because z is the same object as x 

print(x is not y) 
# returns True because x is not the same object as y, even if they have the same content 

print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y

# Python Membership Operators 
# Membership operators are used to test if a sequence is presented in a object:

# in  -  Returns True if a sequence with the specified value is presetn in the object  x in y
x = ["apple", "banana"]
print("banana" in x )
# returns True because a sequence with the value "banana" is in the list

# not in     -  Returns True if a sequence with the specified value is not present in the object  x not in y
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True becuse a sequence with the value "pineapple" is not in the list

# Python Bitwise Operators 
# Bitwise operators are used to compare (binary) numbers:
 
#  &  - AND  -  sets each bit to 1 if both bits are 1 
#  |  - OR   -  sets each bit to 1 if one of two bits is 1
#  ^ -  XOR  -  sets each bit to 1 if only one of two bits is 1
#  ~  - NOT  -  Inverts all the bits 
#  << - Zero fill left shift  - Shift left by pushing zeros in form the right and let the leftmost bits fall off
#  >> - Signed right shift  -  Shift right by pushing copies of the leftmodt bit in form the left, and let the rightmost bits fall off.


