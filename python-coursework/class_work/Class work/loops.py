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

