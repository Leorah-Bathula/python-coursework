#infinite loop 
pin = 1234

while True:
    ent_pin = int(input('0-Exit:'))
    if pin == ent_pin:
        print("Login Successful")
        break
    else:
        print("Invalid login. Try again")

'''
1. Print Numbers from 1 to N (Using for loop)
Problem: Write a program to print numbers from 1 to N using a for loop.
● Input: An integer N
● Output: Numbers from 1 to N.
'''  
n = int(input())

for i in range(1, n + 1):
    print(i)

'''
2. Print Even Numbers from 1 to N (Using for loop)
Problem: Write a program to print all even numbers from 1 to N using a for loop.
● Input: An integer N
● Output: Even numbers from 1 to N.
'''
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

'''
3. Sum of Numbers from 1 to N (Using for loop)
Problem: Write a program to find the sum of numbers from 1 to N using a for loop.
● Input: An integer N
● Output: Sum of numbers from 1 to N.
'''
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)


'''
4. Print Odd Numbers from 1 to N (Using for loop)
Problem: Write a program to print all odd numbers from 1 to N using a for loop.
● Input: An integer N
● Output: Odd numbers from 1 to N.
'''
n = int(input())

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

'''
5. Find Factorial of a Number (Using for loop)
Problem: Write a program to find the factorial of a number using a for loop.
● Input: An integer N
● Output: Factorial of N.
'''
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i  # same as fact = fact * i

print(fact)

'''
6. Print Multiplication Table of N (Using for loop)
Problem: Write a program to print the multiplication table of a number N (up to 10) using a
for loop.
● Input: An integer N
● Output: Multiplication table of N.
'''
n = int(input())

for i in range(1, 11):  # Always go up to 10
    print(f"{n} x {i} = {n * i}")

'''
7. Check Prime Number (Using for loop)
Problem: Write a program to check if a number is prime using a for loop.
● Input: An integer N
● Output: "Prime" if the number is prime, "Not Prime" otherwise.
'''
n = int(input())  # Step 1: Take input from the user

if n <= 1:         # Step 2: Numbers 0 and 1 are NOT prime
    print("Not Prime")
else:
    is_prime = True    # Step 3: Assume the number is prime

    for i in range(2, n):     # Step 4: Check from 2 to n-1
        if n % i == 0:        # If any number divides n perfectly
            is_prime = False  # Then it's not a prime number
            break             # Stop checking further

    if is_prime:
        print("Prime")        # Step 5: If no divisors were found, it's prime
    else:
        print("Not Prime")

'''
8. Sum of Digits of a Number (Using while loop)
Problem: Write a program to find the sum of digits of a number using a while loop.
● Input: An integer n
● Output: Sum of the digits of n.
'''
n = int(input())
sum = 0

while n > 0:
    digit = n % 10       # Get the last digit
    sum += digit         # Add it to the sum
    n = n // 10          # Remove the last digit

print(sum)


'''
8A. Sum of First (N-1) Natural Numbers (Using while loop)

'''
n = int(input())
sum = 0 
i = 0 
while i < n:
    sum += i
    i += 1

print(sum)    

'''
9. Print Fibonacci Sequence up to N Terms (Using for loop)
Problem: Write a program to print the Fibonacci sequence up to N terms using a for loop.
● Input: An integer N
● Output: Fibonacci sequence up to N terms.
'''
n = int(input())

a = 0       # First number
b = 1       # Second number

print("Fibonacci sequence:")
for i in range(n):     # Loop n times
    print(a, end=" ")  # Print current number (a)
    next_term = a + b  # Find next number in the sequence
    a = b              # Move to the next pair
    b = next_term

'''
10. Count Numbers Divisible by 3 (Using for loop)
Problem: Write a program to count how many numbers between 1 and N are divisible by 3
using a for loop.
● Input: An integer N
● Output: Count of numbers divisible by 3.
'''
n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print(count)


'''

'''
   
