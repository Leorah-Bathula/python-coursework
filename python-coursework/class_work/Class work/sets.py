''' Sets
1. Introduction to Sets
● A set is an unordered, mutable collection of unique elements.
● Sets automatically remove duplicate elements.
● Sets are similar to mathematical sets and support operations like union, intersection,
and difference.
● They are useful for storing unique elements and performing fast membership tests.'''

# Create an empty set 
s = set()
print(s)
empty_set = set()
print(empty_set)

# Create a set 
s1 = {3,4,5,67,}
print(s1)

# Set with duplicate elements 
s2 = {33,33,2,1,1,4}
print(s2)

# 2. Set properties 
# Unordered
# Unique elements 
# Mutable 
# Immutable Elements only Elements must be hashable (mutable types like lists cannot be elements).

#s3 = {[6,7,8],90} # Lists are mutable and cannot be added to set 
#print(s3) # Will raise an error 

#3. Operations on Sets
# a. Membership Testing
# b. Union (| or union() method)
# c. Intersection (& or intersection() method)
# d. Difference(- or difference() method)
# e. Symmetric Difference(^ or symmetric_difference() method)
# f. Subset(<= or issubset() method)
# g. Superset(>= or issuperset( ) method)
# h. Disjoint Sets(isdisjoint() method)

''' a. Membership Testing
● Check if an element is present using the in or not in keywords.
● Example:'''
s5 = {8,9,6,7,30}
s6 = {20,79,40,30}
print(9 in s5)
print(87 not in s5)

''' 
b. Union (| or union() method)
● Combines elements from two sets (removes duplicates).
● Syntax: set1 | set2 or set1.union(set2)
● Example:
'''
result = s5 | s6 
print(result)

'''
c. Intersection (& or intersection() method)
● Returns common elements between two sets.
● Syntax: set1 & set2 or set1.intersection(set2)
● Example:
'''
result = s5 & s6
print(result)

'''
d. Difference (- or difference() method)
● Returns elements in the first set but not in the second set.
● Syntax: set1 - set2 or set1.difference(set2)
● Example:
'''
result = s5 - s6 
print(result)


'''
e. Symmetric Difference (^ or symmetric_difference() method)
● Returns elements in either set1 or set2 but not both.
● Syntax: set1 ^ set2 or set1.symmetric_difference(set2)
● Example:
'''

result = s5 ^ s6 
print(result)

'''
f. Subset (<= or issubset() method)
● Checks if all elements of one set are present in another.
● Syntax: set1 <= set2 or set1.issubset(set2)
● Example:
'''
print(s5 <= s6)

'''
g. Superset (>= or issuperset() method)
● Checks if one set contains all elements of another.
● Syntax: set1 >= set2 or set1.issuperset(set2)
● Example:
'''

print(s5 >= s6)

'''
h. Disjoint Sets (isdisjoint() method)
● Returns True if two sets have no common elements.
● Example:
'''
print(s5.isdisjoint(s6))

# 4. Built-in Methods for Sets
s5.add(987)
print(s5)

s5.remove(987)
print(s5)

s5.discard(65) #Removes an element; does not raise an error if the element doesn’t exist
print(s5)

s5.pop()
print(s5)

# update(other_set)
'''It adds all elements from other_set into the original set.

It modifies the original set in-place.

It does not return anything (None).'''
s5.update(s6)
print(s5)

''' 1. intersection_update(other_set)
👉 Keeps only the common elements between the sets.
👉 Modifies the original set in-place. '''


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.intersection_update(set2)
print(set1)

''' 2. difference_update(other_set)
👉 Removes all elements in other_set from the original set. ''' 


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.difference_update(set2)
print(set1)

''' 3. symmetric_difference_update(other_set)
👉 Keeps elements that are in either set but not in both.
👉 Like XOR for sets.'''


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.symmetric_difference_update(set2)
print(set1)


 #1. copy() – Returns a shallow copy of the set

my_set = {1, 2, 3}
new_set = my_set.copy()

print("Original:", my_set)
print("Copied:", new_set)

#2. isdisjoint(other_set) – Returns True if sets have no elements in common

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # True

# 3. issubset(other_set) – Returns True if all elements of the first set are in the second

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))  # True

# 4. issuperset(other_set) – Returns True if all elements of the other set are in the first set

set1 = {1, 2, 3, 4}
set2 = {2, 3}

print(set1.issuperset(set2))  # True


print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
print(sorted(set1))


''' set(iterable) – Converts an iterable into a set
Removes duplicates

Unordered collection

Only stores unique elements '''

# Example 1 : List --> Set 
num = [11,22,22,22,33,33,44]
unique_numbers = set(num)
print(unique_numbers)

#  Example 2: String → Set
name = "Jessie"
char_set = set(name)
print(char_set)

# Example 3: Tuple → Set
t = (10,20,30,40)
converted = set(t)
print(converted)


''' 6. Immutability and Frozensets
● Frozensets are immutable versions of sets.
● Once a frozenset is created, its elements cannot be changed.
● Useful for creating hashable, immutable collections. '''

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)