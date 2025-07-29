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


for i in range(5):
    print(i,end = " ") # 0 1 2 3 4

for j in range(5):
    for i in range(5):
        print(i,end = " ")
    print()   # outside loop rows , inside loops columns
'''
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 

'''        
for j in range(5):
    for i in range(5):
        print("*",end = " ")
    print()    
''' col = 0 1 2 3 4 
# rows = 0 * * * * * 
1 * * * * * 
2 * * * * * 
3 * * * * * 
4 * * * * * 
'''    

#Patterns using nested loops 
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print("*",end = " ")
    print()   
'''
Enter the size: 7
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * *
'''    

# 
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(row,end = " ")
    print()

'''
Enter the size: 5
0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
'''        
#
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col,end = " ")
    print()    
'''
Enter the size: 7
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
'''    

#
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row + 1):
        print("*",end = " ")
    print()  
'''
Enter the size: 7
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
''' 

#
n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n - row):
        print("*",end = " ")
    print()   

'''
Enter the size: 5
* * * * * 
* * * * 
* * * 
* * 
*
'''   
#
n = int(input("Enter the sizez: ")) 
for row in range(n):
    for spaces in range(n-row-1):
        print(" ",end = " ")
    for col in range(row + 1):
        print("*",end = " ")
    print()        

'''
Enter the size: 5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''  

#
n = int(input("Enter the size: "))

for row in range(n):
    for spaces in range(row):
        print(" ",end = " ")
    for col in range(n - row):
        print("*",end = " ")
    print() 

'''
Enter the size: 5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

'''     

#
n = int(input("Enter the size: "))

for row in range(n):
    if row <= n//2:
        for col1 in range(row + 1):
            print("*",end = " ")
            
    else:
        for col2 in range(n-row):
            print("*",end = " ")
    print()   

'''
Enter the size: 7
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
'''

# 
n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1:
            print("*",end = " ")
            
        else:
            print(" ",end = " ")
            
    print()        

'''
Enter the size: 7
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * * 
'''    

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1 or row == n //2:
            print("*",end = " ")
            
        else:
            print(" ",end = " ")
            
    print()  

'''
Enter the size: 5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 

'''

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1 or row == n //2 or col == n//2:
            print("*",end = " ")
            
        else:
            print(" ",end = " ")
            
    print() 
'''
Enter the size: 7
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
'''    

#
n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or  row == n-1 or  col + row == n-1:
            print("*",end = " ")
            
        else:
            print(" ",end = " ")
            
    print()  
'''
# col + row == n - 1 is theb logic here 
Enter the size: 7
* * * * * * * 
          *   
        *     
      *       
    *         
  *           
* * * * * * * 
'''    

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if col == row or  col + row == n-1:
            print("*",end = " ")
            
        else:
            print(" ",end = " ")
            
    print()  
'''
Enter the size: 8
*             * 
  *         *   
    *     *     
      * *       
      * *       
    *     *     
  *         *   
*             * 

'''    

