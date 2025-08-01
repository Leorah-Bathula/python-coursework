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
11. Check if a Number is Palindrome (Using while loop)
Problem: Write a program to check if a number is a palindrome using a while loop.
● Input: An integer n
● Output: "Palindrome" if the number is a palindrome, "Not Palindrome" otherwise.
'''
n = int(input())
original = n         # Store original number
reverse = 0          # Initialize reverse

while n > 0:
    digit = n % 10         # Get last digit
    reverse = reverse * 10 + digit  # Build reverse number
    n = n // 10            # Remove last digit

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


'''
12. Print Multiples of 5 up to N (Using for loop)
Problem: Write a program to print all multiples of 5 up to N using a for loop.
● Input: An integer N
● Output: Multiples of 5 up to N.
'''
n = int(input())

for i in range(1, n + 1):
    if i % 5 == 0:
        print(i)

'''
13. Find the Maximum of Three Numbers (Using for loop)
Problem: Write a program to find the maximum of three numbers using a for loop.
● Input: Three integers a, b, c
● Output: Maximum of a, b, c.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

nums = [a, b, c]           # Step 1: Store all numbers in a list
maximum = nums[0]          # Step 2: Assume first number is the max for now

for num in nums:           # Step 3: Loop through each number in the list
    if num > maximum:      # Step 4: Compare each number with current maximum
        maximum = num      # Step 5: If current number is bigger, update maximum

print("Maximum:", maximum) # Step 6: Print the final max value


'''
14. Print Reverse of a Number (Using while loop)
Problem: Write a program to print the reverse of a number using a while loop.
● Input: An integer n
● Output: Reverse of n.
'''
n = int(input())
reverse = 0

while n > 0:
    digit = n % 10                 # Step 1: Get the last digit
    reverse = reverse * 10 + digit # Step 2: Add the digit to the reverse number
    n //= 10                       # Step 3: Remove the last digit from n

print(reverse)                     # Step 4: Print the final reversed number

'''
15. Sum of First N Natural Numbers (Using for loop)
Problem: Write a program to calculate the sum of the first N natural numbers using a for
loop.
● Input: An integer N
● Output: Sum of numbers from 1 to N.
'''
n = int(input())
sum = 0 
for i in range(1, n + 1):
    sum += i
print(sum)

'''
16. Print Numbers from N to 1 (Using while loop)
Problem: Write a program to print numbers from N to 1 using a while loop.
● Input: An integer N
● Output: Numbers from N to 1.
'''
n = int(input())

while n >= 1:
    print(n, end=" ")
    n -= 1

'''
17. Find Sum of Prime Numbers up to N (Using for loop)
Problem: Write a program to find the sum of all prime numbers between 1 and N using a for
loop.
● Input: An integer N
● Output: Sum of all prime numbers between 1 and N.
'''
n = int(input())
sum_primes = 0

for num in range(2, n + 1):  # Start from 2, because 1 is not a prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check for factors
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print(sum_primes)


'''
18. Find the Product of Digits of a Number (Using while loop)
Problem: Write a program to calculate the product of the digits of a number using a while
loop.
● Input: An integer n
● Output: Product of digits of n.
'''
n = int(input())
product = 1

while n > 0:
    digit = n % 10         # Get the last digit
    product *= digit       # Multiply the digit to the product
    n //= 10               # Remove the last digit

print(product)

'''
19. Print Numbers Divisible by Both 3 and 5 (Using for loop)
Problem: Write a program to print all numbers divisible by both 3 and 5 up to N using a for
loop.
● Input: An integer N
● Output: Numbers divisible by both 3 and 5.
'''
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} is divisible by both 3 and 5")
    else:
        print(f"{i} is not divisible by both 3 and 5")

'''
20. Find GCD of Two Numbers (Using while loop)
Problem: Write a program to find the GCD of two numbers using a while loop.
● Input: Two integers a and b
● Output: GCD of a and b.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Start from the smaller number
i = min(a, b)

while i > 0:
    if a % i == 0 and b % i == 0:
        print("GCD is:", i)
        break
    i -= 1

'''
21. Print Right-Angled Triangle Pattern (Using for loop)
Problem: Write a program to print a right-angled triangle pattern of stars (*) using a for
loop.
● Input: An integer N
● Output: A right-angled triangle pattern of stars.
'''
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):  # i goes from 1 to n
    for j in range(i):     # j goes from 0 to i-1
        print("*", end="  ")
    print()

# for numbers 
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()
'''1  
1  2  
1  2  3  
1  2  3  4  
1  2  3  4  5 '''

'''22. Print Hollow Square Pattern (Using for loop)
Problem: Write a program to print a hollow square pattern using a for loop.
● Input: An integer N
● Output: Hollow square pattern of size N.'''

n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        # Print * for first/last row or first/last column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to next line

'''
23. Check if a Number is Perfect (Using for loop)
Problem: Write a program to check if a number is perfect using a for loop.
● Input: An integer N
● Output: "Perfect" if the number is perfect, "Not Perfect" otherwise.
'''



    


