''' import re

pattern = r"Hello"

res = re.match(pattern,"Hello world")
print(res.group() if res else "No match")'''

# match --> to check whether your string is starting with a pattern
import re

pattern = r"[aeiou]"

res = re.match(pattern,"Hello world")
print(res.group() if res else "No match")

import re

pattern = r"[A-Z]"

res = re.match(pattern,"Hello world")
print(res.group() if res else "No match")

import re

pattern = r"\d" # for integers 

res = re.match(pattern,"18Hello world")
print(res.group() if res else "No match")

# search 
import re 

pattern = r"[aeiou]"

res = re.search(pattern,"hello world")

print(res.group() if res else "no match") # e

import re 

pattern = r"[aeiou]"

res = re.findall(pattern,"hello world")

#print(res.group() if res else "no match")
print(res)  # ['e', 'o', 'o']

import re 

pattern = r"\d{4}|\d{2}"

res = re.findall(pattern,"pfs-31 2025 pfs-14 2024 pfs-10 2023")

#print(res.group() if res else "no match")
print(res) # ['31', '2025', '14', '2024', '10', '2023']

import re 

pattern = r"\d{4}|\d{2}"

res = re.finditer(pattern,"pfs-31 2025 pfs-14 2024 pfs-10 2023")
for i in res:
    print(i.group(),i.start())
'''
31 4
2025 7
14 16
2024 19
10 28
2023 31
'''

import re 

pattern = r"\d{10}"

res = re.fullmatch(pattern,"202456868530")
print(res.group() if res else "no match") # no match

# sub
import re 
pattern = r"[A-Z]"
res = re.sub(pattern,"@","Python Programming Language")
print(res) # @ython @rogramming @anguage


# . (Matches any character (except newline))
import re 
pattern = r"h.t"
res = re.findall(pattern,"hot hat hit hood wood hid ")
print(res) # ['hot', 'hat', 'hit']


# ^ Matches start of a string 
import re 

pattern = r"^g..d$"

res = re.findall(pattern,"good")

print(res)


import re 

pattern = r"\w*"

res = re.findall(pattern,"good")

print(res)


#()
import re 

pattern = r"(aeiou\d{3})"

res = re.findall(pattern,"aeiou679")

print(res)



    



    



    

