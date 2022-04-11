# Slicing 
# You can returna range of characters from position 2 to position 5 (not included):
b = "Hello, World"
print(b[2:5])

# Note first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:4

# Get the characters from the start to position 5 (not included)

b = "Hello, World!"
print(b[:5])

# Slice to the End 
# By leaving out the end index, The range will go to the end:

# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# get the characters:
# From: "0" in "World!" (position - 5)
# To, but not included: "d" in "World!" (position - 2):

b = "Hello, World!"
print(b[-5:-2])



