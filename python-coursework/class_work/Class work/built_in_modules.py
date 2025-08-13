'''
import sys
print(sys.argv)
['']
print(sys.path)
['', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\idlelib', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\DANNY\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
print(sys.version)
3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]
print(sys.exit())
'''
'''
import platform
print(platform.system())
Windows
print(platform.release())
11
print(platform.processor())
Intel64 Family 6 Model 158 Stepping 10, GenuineIntel

'''

'''
import math
print(math.pi)
3.141592653589793
print(math.e)
2.718281828459045
print(math.asinh)
<built-in function asinh>
print(math.sqrt(25))
5.0
print(math.pow(3,3))
27.0
print(round(12.3))
12
print(round(12.8))
13
print(math.ceil(12.3))
13
print(math.ceil(12.8))
13
print(math.ceil(12.001))
13
print(math.floor(12.3))
12
print(math.ceil(12.8))
13
print(math.floor(12.3))
12
print(math.floor(12.999))
12
print(abs(-13))
13
print(abs(-12.4))
12.4
print(math.fabs(-13))
13.0


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(5))
SyntaxError: invalid syntax
print(math.factorial(5))
120
print(math.gcd(8,12))
4
print(math.log(2))
0.6931471805599453
print(math.log(2,2))
1.0
print(math.sin(45))
0.8509035245341184
print(math.cos(45))
0.5253219888177297
print(math.tan(45))
1.6197751905438615
KeyboardInterrupt
print(math.degrees(45))
2578.3100780887044
print(math.radians(45))
0.7853981633974483

n1 = int(input())
n2 = int(input())

n= min(n1,n2)

for i in range(n,0,-1):
    if n1 % i == 0 and n2 % i == 0:
        print(f"GCD({n1},{n2}): {i}")
        break


#3.2 random – Generate Random Numbers
import random
print(random.random())
0.556032559533173

print(random.randint(1,10))
5

l = ["apple","papaya","melon","grapes"]
print(random.choice(l))
papaya

print(random.uniform(1,5))
1.322099519216327

print(random.choices(l,k = 2))
['papaya', 'apple']

random.shuffle(l)
print(l)
['grapes', 'apple', 'melon', 'papaya']

random.seed(10)
print(random.uniform(1,5))
3.285610378759654
print(random.randint(1,10))

#4.2 itertools – Efficient Iteration Utilities
from itertools import combinations,permutations
s = "Leorah"
s1 = "apple"

t = ('a','b','c')
''.join(t)
'abc'

t = tuple(combinations(s1,3))
t
(('a', 'p', 'p'), ('a', 'p', 'l'), ('a', 'p', 'e'), ('a', 'p', 'l'), ('a', 'p', 'e'), ('a', 'l', 'e'), ('p', 'p', 'l'), ('p', 'p', 'e'), ('p', 'l', 'e'), ('p', 'l', 'e'))
for i in t:
    print(''.join(i),end = ",")

    
app,apl,ape,apl,ape,ale,ppl,ppe,ple,ple,

p = tuple(permutations(s,2))
p
(('L', 'e'), ('L', 'o'), ('L', 'r'), ('L', 'a'), ('L', 'h'), ('e', 'L'), ('e', 'o'), ('e', 'r'), ('e', 'a'), ('e', 'h'), ('o', 'L'), ('o', 'e'), ('o', 'r'), ('o', 'a'), ('o', 'h'), ('r', 'L'), ('r', 'e'), ('r', 'o'), ('r', 'a'), ('r', 'h'), ('a', 'L'), ('a', 'e'), ('a', 'o'), ('a', 'r'), ('a', 'h'), ('h', 'L'), ('h', 'e'), ('h', 'o'), ('h', 'r'), ('h', 'a'))
for i in p:
    print(''.join(i),end = ",")

    
Le,Lo,Lr,La,Lh,eL,eo,er,ea,eh,oL,oe,or,oa,oh,rL,re,ro,ra,rh,aL,ae,ao,ar,ah,hL,he,ho,hr,ha,




'''
from collections import deque,defaultdict,Counter

s = "Hello world Python Program"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:    
        d[i] = 1
print(d)

freq = Counter(s) # Counter how many times the letter is repeating
print(freq)

'''{'H': 1, 'e': 1, 'l': 3, 'o': 4, ' ': 3, 'w': 1, 'r': 3, 'd': 1, 'P': 2, 'y': 1, 't': 1, 'h': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1}
Counter({'o': 4, 'l': 3, ' ': 3, 'r': 3, 'P': 2, 'H': 1, 'e': 1, 'w': 1, 'd': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1})'''

from collections import deque,defaultdict,Counter

s = [1,2,3,4,5,6,7,8,9,1,2,3,4,4]

freq = Counter(s) # Counter how many times the letter is repeating
print(freq)

'''
Counter({4: 3, 1: 2, 2: 2, 3: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
'''
from collections import deque,defaultdict,Counter

s = [1,2,3,4,5,6,7,8,9,1,2,3,4,4]
d = defaultdict(int)
d[1] = d[1] + 1
print(d)

'''
defaultdict(<class 'int'>, {1: 1})
'''

from collections import deque,defaultdict,Counter

s = [1,2,3,4,5,6,7,8,9,1,2,3,4,4]

d = defaultdict(int)
for i in s:
    d[i] += 1
print(d)

# defaultdict(<class 'int'>, {1: 2, 2: 2, 3: 2, 4: 3, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})

# deque
from collections import deque,defaultdict,Counter

d = deque()
d.appendleft(12)
d.pop()

d.append(12)
d.popleft()

print(d)
# deque([])

