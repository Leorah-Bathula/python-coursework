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


# 4.String testing methods
y = "CloudySkies"
print(y.startswith("Clo")) #startswith(sub) Checks if the string starts with sub.
print(y.endswith("ies")) #endswith(sub) Checks if the string ends with sub.
print(y.isalpha()) #isalpha() Returns True if all characters are alphabets.
print(y.isalnum()) # isalnum() Returns True if all characters are alphanumeric.
# An alphanumeric character is a character that can be a letter (A-Z, a-z) or a number (0-9). It combines alphabetic and numeric characters. 
print(y.islower()) # islower()  Returns True if all characters are lowercase.
print(y.isupper()) # isupper() Returns True if all characters are uppercase.
print(y.isspace()) # isspace() Returns True if all characters are whitespace.
print(y.istitle()) # istitle() Returns True if the string is in the title case.
print(y.isidentifier()) # isidentifier() Checks if the string is a valid Python identifier.
print(y.isdecimal())  # Most strict; only base-10 digits ('0'–'9' and equivalents)
print(y.isdigit()) # Allows additional digit characters like superscripts
print(y.isnumeric()) # Checks if the string is a valid Python identifier.

# 5. Replace and Modify Methods 
print(y.replace("Cloudy","Cotton")) #replace(old,new) Replaces occurrences of old with new.

# maketrans() Creates a translation table for translate().
# translate(table) Replaces characters using a translation table.
# create a transition table 
table = str.maketrans("aeio","@310")

# Apply translation to string 
text = "Hello , my name is Jessie"
translated = text.translate(table)
print(translated)  # H3ll0 , my n@m3 1s J3ss13

# 6. Splitting and joining methods
z = "I,Love,Cookies"
print(z.split(","))  # ['I', 'Love', 'Cookies'] Splits the string into a list by sep.
# split(sep, 1)	Left to right	1 split
print(z.rsplit(",",1)) # ['I,Love', 'Cookies']
# rsplit(sep, 1)	Right to left	1 split Splits from the right side.

k = "New\nYork\nCity"
print(k.splitlines()) # Splits at line breaks (\n). ['New', 'York', 'City']

# join() It joins elements of an iterable (like a list or tuple) into a single string, using the string you call it on as a separator.
# Example 1: Joining words with space 
words = ["I","Love","Chips"]
sentence = " ".join(words)
print(sentence)  # I Love Chips

#  Example 2: Joining with hyphen
items = ["apple" ,"banana","cherry"]
result = "-".join(items)
print(result) # apple-banana-cherry

# Example 3: Joining with no separator (combine chars)
chars = ['J', 'e', 's', 's', 'i', 'e']
name = "".join(chars)
print(name) # Jessie

j = "apple-pieday"
print(j.partition("-"))  # ('apple', '-', 'pieday') Splits into a 3-part tuple at first sep. (before, sep, after) from first match
o = "pine-apple-day"
print(o.rpartition("-")) # ('pine-apple', '-', 'day') Splits into a 3-part tuple at lastsep. 	(before, sep, after) from last match

# 7. Whitespace & Trimming Methods

s = "    Hello Jessie    "
print(s.strip()) # Hello Jessie Removes leading and trailing characters (default: spaces).
print(s.lstrip()) # Hello Jessie    Removes leading characters.
print(s.rstrip()) #     Hello Jessie Removes trailing characters.

# 8. Encoding & Decoding Methods
#  encode() Encode a string to bytes
text = "Hello Leorah"
encoded = text.encode("utf-8")
print(encoded) # b'Hello Leorah'

# decode() Decode bytes back to string
decoded = encoded.decode("utf-8")
print(decoded) # Hello Leorah








