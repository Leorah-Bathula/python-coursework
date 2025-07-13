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

