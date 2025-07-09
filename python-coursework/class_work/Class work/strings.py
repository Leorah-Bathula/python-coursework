#A string is a sequence of characters enclosed within single quotes (' '), double quotes (""), or triple quotes (''' ''' or """ """).

a = "Apple"
b = "Orange"
c = "Watermelon"

print(a)
print(b)
print(c)

''' Operations on Strings
1. Concatenation (+) - Joining two or more strings.
2. Repetition (*) - Repeating a string multiple times.
3. Indexing - Accessing individual characters using indices.
4. Slicing - Extracting a part (substring) of the string.
5. Membership (in, not in) - Checking if a substring exists within a string. '''

# Concatenation
d = "Jessie"
e = "Leorah"
result = d + " " + e
print(result)

# Repititon 
print("Leo" * 3)

# Indexing
d = "Jessie"
print(d[0])
print(d[4])
print(d[-1])

# Slicing
print(d[0:4]) #Jess
print(d[:5]) #Jessi
print(d[2:]) #ssie
print(d[1:5:1]) #essi
# sequence[start : stop : step]
#J  e  s  s   i  e 
#-6 -5 -4 -3 -2 -1
print(d[-1]) #e
print(d[-3:]) #sie
print(d[:-3]) #Jes

print(d[::-1])  #Reverse eisseJ
print(d[-1:-5:-1])  #eiss
print(d[1:-1])  #essi

# Membership 
print("Jes" in d ) # True
print("Tom" in d) # False
print("Leo" not in d) # True

''' 
Built-in String Functions
While string methods are called on string objects, Python also provides some built-in
functions that work with strings:
1. len() - Returns the length of the string.
2. max() / min() - Returns the maximum or minimum character (based on ASCII
values).
3. sorted() - Returns a sorted list of characters.
4. chr() / ord() - Converts between characters and their ASCII codes.


'''
# 1. len()
e = "Leorah"
print(len(e)) 

# 2. max() and min()
print(max("KittyCandy")) # 'y' (highest ASCII VALUE)
print(min("KittyCandy")) # 'C' (lowest ASCII VALUE)

# 3. sorted()
print(sorted("CrystalPearl")) #['C', 'P', 'a', 'a', 'e', 'l', 'l', 'r', 'r', 's', 't', 'y']

# 4. chr() and ord()
print(ord('B')) # 66 (ASCII value of 'A')
print(chr(77))  #  M (character for ASCII value 97)

#Complete List of Python String Methods with Examples

#1. Case Conversion Methods

print(d.upper())
print(d.lower())
print(d.capitalize())  #Capitalizes the first character.
print(d.title()) #Capitalizes the first letter of each word
print(d.swapcase()) #Swaps case: upper → lower, lower→ upper.
print(d.casefold()) #Converts to lowercase (more aggressive than lower()).

# 2. Alignment and Formatting Methods
f = "Rainbow"
print(f.center(10, "*"))  #Centers the string within width.
print(f.ljust(10, "-"))   # → Rainbow--- Left-aligns the string within width.
print(f.ljust(12, "-"))   # → Rainbow-----
print(f.rjust(10, "*")) # ***Rainbow Right-aligns the string within width.
print(f.zfill(14)) # Pads the string with zeros on the left.
print("Name: {}, Age: {}".format("Tom", 32)) #Formats strings dynamically. Name: Tom, Age: 32
print("{name} is {age}".format_map({'name' :'Ricky' , 'age' : 25}))  #Formats using a dictionary. Ricky is 25


# 3. Search & Find Methods

x = "applepie"
print(x.find("p")) # 1 (Returns the index of first occurrence, -1 if not found.)
print(x.rfind("p")) # 5 (Returns the last occurrence of the substring.)
print(x.index("l")) # 3 (Like find(), but raises an error if not found.)
print(x.rindex("p")) # 5 (Like rfind(), but raises an error if not found.)
print(x.count("p")) # 3 (Counts how many times 'p' appears.)
