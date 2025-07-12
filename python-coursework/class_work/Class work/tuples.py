'''Tuples
1. Introduction to Tuples
● A tuple is an immutable, ordered collection of elements.
● Tuples are similar to lists, but once a tuple is created, its contents cannot be
changed.
● Tuples can store any type of data (int, float, string, list, etc.).
● Tuples are faster than lists because they are immutable.'''

# Create a tuple 
t = ()
t = tuple()
print(t)

# Single-element tuple 
single_tuple = (7,)
print(single_tuple)

# Multi-element Tuple
my_tuple = (4,"Orange", 4.9)
print(my_tuple)

# Without parentheses (implicit tuple creation)
implicit_tuple = 1,2,4,5
print(implicit_tuple)

# 2. Accessing Tuple Elements
# a. Indexing
# b. Negative Indexing
# c. Slicing

# a. Indexing
t1 = (20,40,60,80,90)
print(t1[4])
print(t1[-4]) # Negative Indexing
print(t1[2:5]) # Slicing

# 3. Operations on Tuples
# a. Concatenation
# b. Repetition
# c. Membership Testing
# d. Tuple Unpacking

# a. Concatenation Combine two or more tuples using the + operator.
t1 = (20,40,60,80,90)
t2 = (50,30,20,10,100)
new_tuple = t1 + t2 
print(new_tuple)

# b. Repetition ● Repeat the elements of a tuple using the * operator.
t3 = (9,8,7)
print(t3 * 3)

# c. Membership Testing ● Check if an element is present in the tuple using the in or not in keywords.
t4 = (55,33,49)
print(33 in t4)
print(89 not in t4)

# d. Tuple Unpacking ● Assign tuple elements to multiple variables.
t5 = (70,80,120)
a, b, c = t5
print(a,b,c)

# 4. Tuple Methods
t6 = (5,5,5,9,2,1)
print(t6.count(5)) # 3 Counts the number of occurrences of x in the tuple
print(t6.index(5)) #  0 Returns the first index of x in the tuple

# 5. Built-in Functions for Tuples
print(len(t6))
print(max(t6))
print(min(t6))
print(sum(t6))

# tuple(iterable) it simply converts any iterable (like a list or string) into a tuple 

#  Example 1: Convert a list to a tuple
numbers = [1,2,3]
t = tuple(numbers)
print(t)

# Example 2: Convert a string to a tuple
name = "Jessie"
t = tuple(name)
print(t)

# Example 3: Convert a range to a tuple
r = range(5)
t = tuple(r)
print(t)

#  Example 4: Convert a set to a tuple
s = {20,30,40}
t = tuple(s)
print(t)

# 6. Immutability and Tuple Behavior
''' Since tuples are immutable:
● You cannot modify elements (tuple[0] = 10 will raise an error).
● However, if a tuple contains mutable objects (e.g., lists), the mutable objects can still
be changed. '''

nested_tuple = (1,[2,3])
nested_tuple[1][0] = 3
print(nested_tuple) # (1, [3, 3])

# nested_tuple[0] = 3
# print(nested_tuple) # will raise an error).


# 7. Advantages of Tuples
''' 1. Immutability: Ensures data cannot be accidentally modified.
2. Faster: Tuples are more memory-efficient and faster than lists.
3. Hashable: Tuples can be used as keys in dictionaries (unlike lists).
4. Data Integrity: Ideal for storing constant data. '''

#  1. Convert a tuple → list
# Use the list() function:
t = (1,2,3)
converted_list = list(t)
print(converted_list) # [1, 2, 3]

# 2. Convert a list → tuple
# Use the tuple() function:
l = [4,5,6]
converted_tuple = tuple(l)
print(converted_tuple) # (4, 5, 6)




