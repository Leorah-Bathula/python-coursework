d = {"Name": "Leorah","Age" : 21 , "Course": "Python"}
print(d)

# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
#Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.

# Key Features of Dictionaries:

''' 1. Keys must be unique
2. Keys must be immutable
3. Values can be of any data type
4. Dictionaries are mutable '''

# 2. Dictionary Operations
# 2.1 Accessing Values

print(d["Name"])
print(d.get("Age"))

#dict[key] raises keyerror if the key  does not exist
#dict.get(key,default_value) will return None or the specified default_value if the key is not found.

print(d.get("Color","Not Available"))

# 2.2 Adding and Updating Items
d["Age"] = 20 # update existing key 
d["City"] = "New York" # Adding a new key-value pair 
print(d)

# 2.3 Removing Items from a Dictionary
# ways to remove elements from a dictionary 
# pop(key)
# del 
# popitem()
# clear()

#Using pop(key)
#Removes the specified key and returns its value.
Age = d.pop("Age")
print(Age) # 20 
print(d)

#Using del --> Deletes a specific key-value pair or the entire dictionary.
del d["Course"]
print(d)

#Using popitem() --> Removes and returns the last inserted key-value pair.
d.popitem()
print(d)

# Using clear() --> Removes all key-value pairs, making the dictionary empty.
d.clear()
print(d) # {}


d = {"Name": "Leorah","Age" : 21 , "Course": "Python"}
print(d)
# 3.1 Dictionary Methods for Accessing Data
print(d.keys())
print(d.values())
print(d.items()) #Returns a view object containing all key-value pairs as tuples

# 3.2 Dictionary Methods for Adding and Updating Data
print(d.update({"City":"New York"}))
print(d)
print(d.setdefault("Day","Unknown"))

#4. Built-in Functions for Dictionaries
print(len(d))
print(max(d))
print(min(d)) # returns alphabetcial wise 
print(sorted(d)) # Returns sorted list of keys

#5. Nested Dictionaries
#A dictionary can contain another dictionary as its value.

students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) # Output: CS

# 1. Add Multiple Key-Value Pairs at Once
student = {"name":"leorah"}
student.update({"age":22,"course":"AI","college":"Anurag University"})
print(student)
# output : {'name': 'Jessie', 'age': 22, 'course': 'AI', 'college': 'Anurag University'}

#  2. Store Multiple Values Under One Key (using a list)
student = {"skills":["python","SQL","AI"]}
student["skills"].append("Machine Learning")
print(student)

# To keep everything in one dictionary 
student = {"name" : "leorah"}
student.update({"age":22,"course":"AI","college":"Anurag University"})

# Add skills key with multiple values 
student["skills"] = ["python","SQL","AI"]

#Add more skills 
student["skills"].append("Machine learning")

#print the whole dictionsary
print(student)

'''
output:
{
  'name': 'leorah',
  'age': 22,
  'course': 'AI',
  'college': 'Anurag University',
  'skills': ['python', 'SQL', 'AI', 'Machine Learning']
}

'''

#3. Loop to Add Multiple Items Dynamically
data = {}

for i in range(3):
    key = input("Enter key: ")
    value = int(input("Enter a value: "))
    data[key] = value

print(data)    

# 4. Dictionary of Lists (Multiple values for multiple keys)
student = {
    "name" : ["Jessi","Ales"],
    "age" : [22,21],
    "course" : ["AI","DS"]
}

student["name"].append("Riya")
print(student)
# O/P : {'name': ['Jessie', 'Alex', 'Riya'], 'age': [22, 21], 'course': ['AI', 'DS']}

'''
GOAL   ---->   WHAT TO USE
Add several key-value pairs --->  dict.update() or merging
One key , many values ---> Use a list as the value 
Dynamically build dictionary --> Loop + dict[key] = value 

'''

# Dictionary Comprehensioon 
# You can create dictionaries dynamically using dictionary comprehension.

squares = {x: x*x for x in range(1,6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Problem 1: Count the Frequency of Words in a Sentence
sen = "hello world hello python"
word_count = {}

for word in sen.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)        
# # Output: {'hello': 2, 'world': 1, 'python': 1}

# Problem 2: Find the Student with the Highest Marks
students = {
"Alice": 85,
"Bob": 92,
"Charlie": 88
}

top_student = max(students, key = students.get)
print(top_student) #Bob

