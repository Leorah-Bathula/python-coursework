# Prime number or not
n = int(input("Enter the number: "))
isprime = False 
for i in range(2,n//2 + 1):
    if n % i == 0:
        isprime = True
        break
if isprime:
    print("Not a prime number")
else:
    print("prime number")

#using count 
n = int(input("Enter the number: "))
count = 0
for i in range(2,n//2 + 1):
    if n % i == 0:
        count = 1
        break
if count:
    print("Not a prime number")
else:
    print("prime number")

#Factorial of a number
n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i 
print(f"{n}! = {fact}")    

#Sum of numbers
n = int(input("Enter the number: "))
sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)  


#***WHILE LOOPS PROGRAMS***
# While loop candy crush game 
moves = 34
winningpoint = int(input("Enter the winning point: "))


while moves > 0:
    if moves == winningpoint:
        print("Congrats!!you win the game ")
        break
    print(f"{moves} are left. You have chance to win the game")
    moves -= 1
else:
    print("Game over. Try again")

# iteration through string
s = "python programming"
ind = 0
n = len(s)
while ind < n:
    
    print(ord(s[ind]),end = " ")
    ind += 1

# iteration through list
l = [1,2,3,4,5]
ind = 0 
while ind<len(l):
    print(l[ind])
    ind += 1        

# iteration through tuple
l = (1,2,3,4,5)
ind = 0 
while ind<len(l):
    print(l[ind])
    ind += 1    


# 5 4 3 2 1
n = 5
while n > 0:
    print(n)
    n -= 1

'''3
6
9
12
15
18 3 tables multiplication'''
n = 3
while n < 19:
    print(n)
    n = n + 3

n = 1
while n < 10:
    print(n * 3)
    n = n + 1

 # squares 
n = 1
while n < 7:
    print(n **2)
    n += 1

#cubes
n = 1
while n < 7:
    print(n **3)
    n += 1 

# 10 20 30 = 60(adding in list)
l = list(map(int,input().split()))

s = 0 
ind = 0 

while ind < len(l):
    s = s + l[ind]
    ind += 1
print(s) 


# 234567 = 27 (add)

n = int(input())
s = 0
while n > 0:
    s += (n%10)
    n//=10
    
print(s)    

# palindrome 12321
n = int(input())
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + (n%10)
    n //= 10
    
if rev == temp:
    print("palindrome")
else:
    print("Not palindrome")

# 
n = input()
if n == n [::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

#
n = input()
full = len(n) - 1
length = len(n) // 2
ind = 0 

while ind <= length:
    if n[ind] != n[full]:
        print("Not palindrome")
        break
  
    ind += 1 
    full -= 1 
    
else:
    print("Palindrome ")        