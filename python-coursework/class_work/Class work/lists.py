# Create a list 
l = []
l = list()
print(l)

# Basic Features of Lists
# Ordered,Mutable,Indexed,Allow Duplicates,Heterogeneous,Dynamic

# List with elements
num = [2,3,4,5,6,7]
colours = ["Blue","Pink","Green","White","Gold"]
mixed = [34,50.8,"Python",True] #Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).

nested_list = [[1,2,3],["a","b","c"],[True,False]]

print(num)
print(colours)
print(mixed)
print(nested_list)

# List using list() Constructor
list_from_tuple = list((1,2,3))  # Converting tuple to list [1, 2, 3]
string_to_list = list("Jessie")  # ['J', 'e', 's', 's', 'i', 'e']
print(list_from_tuple)
print(string_to_list )

#3. Accessing Elements in a List
#3.1 Using Indexing (Positive & Negative)
#3.2 Using Slicing

#3.1 Using Indexing (Positive & Negative)
subjects = ["English","Hindi","Telugu","Tamil"]
print(subjects[3])
print(subjects[2])
print(subjects[-1])

#3.2 Using Slicing
print(subjects[1:4])
print(subjects[::-1])
print(subjects[2:3])

# 4. Modifying Lists
# 4.1 Changing Elements
num = [2,3,4,5,6,7]
num[2] = 40
print(num)

# 4.2 Adding Elements
num.append(50)
num.insert(2,70)
num.extend([88,32,43])
print(num)

# 4.3 Removing elements 
num.remove(50) # Removes first occurrence of 100
num.pop(4) # # Removes element at index 4
num.pop() # Removes last element
del num[1] # Deletes element at index 1
print(num)

# 5. List Methods
i= num.index(88)  #Returns the index of the first occurrence of x.
print(i)

print(num.count(6))

numbers = [90,34,23,20]
numbers.sort() # ascending order
print(numbers)
numbers.sort(reverse=True) # descending order
print(numbers)
numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)

# 6. Copying a List
# Shallow Copy
list1 = [1,2,3]
list2 = list1.copy()
print(list2)

print(min(list1))
print(max(list1))
print(sum(list1))
print(any(list1)) #Returns True if at least one element is True in the list.
print(all(list1)) # Returns True if all elements are True in the list.
print(len(list1))