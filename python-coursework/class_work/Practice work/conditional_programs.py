hr,mins = list(map(int,input("Enter the HH:MM  :").split(":")))

if hr >= 0 and hr <= 24 and mins > 0 and mins <= 60 :
    if hr >= 0 and hr < 4:
        print("It's high time. Time to sleep")
    elif hr >= 4 and hr < 12:
        print("Good morning! Have a nice day ")
    elif hr >= 12 and hr < 16:
        print("Good afternoon! Yum Lunch time")
    elif hr >= 16 and hr < 20:
        print("Good evening! Play time")
        
    elif hr >= 20 and hr < 24:
        print("Good night!Time to sleep")

else:
    print("Enter the proper input , invalid input !")

    
#2 To check the number of seats availble using if else:
seats = {
    'L1': True,
    'L2': False,
    'L3': True,
    'L4': True,
    'L5': False,
    'U1': True,
    'U2': False,
    'U3': True,
    'U4': True,
    'U5': False,
    
}

seat_no = input("Enter the seat number to check its availabilty: ").upper()

if seat_no in seats:
    if seats[seat_no]:
        print("Already Booked. Try with other number")
        
    else:
        print("Seat is available. Hurry up")
else:
    print("Enter the correct seat number")
        

# Check the product availablity using if-else:
data = {
    'watch' :  {'discount':10, 'brands':['titan','fastrack']},
    'jeans' :  {'discount':60, 'brands':['denim','roadster']},
}

print(data.keys())
product = input("Enter the category: ")

if product in data:
    print(f"{data[product]["discount"]} % discount is going on for this brands {data[product]["brands"]}")
        
else:
    print(f"Product is not available. Check other products: {data}")            


# movie selection 
movies = {
    'Salar' :  {'kids' : True},
    'Starr' :  {'kids' : True},
    'Arjunreddy' : {'kids' : False},
    'Teddy' :  {'kids' : False}
    
}

print("Welcome to hotstar".center(30,"="))
movie = input("ENter the movie name: ").title()

if movie in movies:
    if movies[movie]["kids"]:
        print(f"Good selection you can watch with your family\n{movie}...")
    else:
        print(f"Adult movie kids are not allowed\n{movie}...")
        
else:
    print(f"{movie} is not availble")
    

'''  1. Positive or Negative
● Input: 5
● Output: Positive number  '''
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")

elif num < 0:
    print("Negative number")
    
else:
    print("Zero")


''' 2. Even or Odd
● Input: 8
● Output: Even number
'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


'''
3. Divisible by 5
● Input: 15
● Output: Divisible by 5
'''
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

'''
4. Divisible by 3 and 7
● Input: 21
● Output: Divisible by both 3 and 7

'''
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")

'''
5. Check for Leap Year
● Input: 2024
● Output: Leap year
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
  print("Leap Year")

elif year % 100 == 0 :
  print("Not a leap year")

elif year % 4 == 0:
  print("Leap year")

else:
  print("Not a leap year")

  '''
  6. Check Pass or Fail (Passing marks = 35)
● Input: 40
● Output: Pass
  '''
  n = int(input("Enter a number: "))
if n >= 35:
    print("Pass")
else:
    print("Fail")

'''
7. Check if number is 3-digit
● Input: 123
● Output: 3-digit number
'''
n = input("Enter a number: ")
print(len(n))

if (len(n) == 3):
    print(f"{n} is a 3-digit number")
else:
    print(f"{n} is not a 3-digit number")

# But if the user enters a negative number, like -45, then len(n) will be 3 ('-45') — which is wrong logically.
n = int(input("Enter a number: "))
if 100 <= abs(n) <= 999:
    print(f"{n} is a 3-digit number")
else:
    print(f"{n} is not a 3-digit number")    

'''
8. Check if character is vowel
● Input: a
● Output: Vowel
'''
n = input("Enter a character: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if n in vowels:
    print("Vowel")
else:
    print("Not vowel")

'''
9. Check greatest of two numbers
● Input: 7, 9
● Output: 9 is greater
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both numbers are equal")

'''
10. Check smallest of two numbers
● Input: 3, 8
● Output: 3 is smaller
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(f"{a} is smaller")
elif b < a:
    print(f"{b} is smaller")
else:
    print("Both numbers are equal")

'''
11. Check if number is zero
● Input: 0
● Output: Number is zero
'''

n = int(input("Enter a number: "))
if n == 0:
    print("Number is Zero")
else:
    print("NUmber is not zero")

'''
12. Check if number is multiple of 10
● Input: 50
● Output: Multiple of 10
'''    
n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Multiple of 10")
else:
    print("Not Multiple of 10")

'''
13. Check if age is eligible to vote (18+)
● Input: 19
● Output: Eligible to vote
'''  
age = int(input("Enter a number: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

'''
14. Check if number is between 1 and 100
● Input: 45
● Output: In range
'''    
n = int(input("Enter a number: "))

if n >= 1 and n <= 100:
    print("In range")
else:
    print("Not in range")


'''
15. Check if number is square of another
● Input: 4, 2
● Output: 4 is square of 2
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b ** 2:
    print(f"{a} is square of {b}")
elif b == a ** 2:
    print(f"{b} is square of {a}")
else:
    print("Neither number is a square of the other")

'''
16. Check if two strings are equal
● Input: "apple", "apple"
● Output: Strings are equal
'''    
a = input("Enter the name1: ")
b = input("Enter the name2: ")

if a == b:
    print("Strings are equal")
else:
    print("Strings are not equal")

'''
17. Check if a number is prime (basic logic)
● Input: 7
● Output: Prime number
'''    
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

'''
18. Check if number is positive and even
● Input: 12
● Output: Positive and even number
'''    
n = int(input("Enter a number: "))
if n > 0 and n % 2 == 0:
    print("Positive and even number")
else:
    print("Not positive and even number")

'''
19. Check if character is uppercase
● Input: "A"
● Output: Uppercase letter
'''
n = input("Enter a character: ")

if n.isupper():
    print("Uppercase letter")
else:
    print("Not uppercase")

'''
20. Check if temperature is hot (>30°C)
● Input: 35
● Output: It's hot
'''   
n = int(input("Enter the temperature in °C: "))
if n > 30:
    print("It's hot")
else:
    print("Not hot")

'''
1. Check if a number is a 4-digit even number
Input: 2468
Expected Output: 4-digit even number
'''
n = int(input("Enter a number: "))
if len(str(n)) == 4 and n % 2 == 0:
    print("4-digit even number")
else:
    print("Not 4-digit even number")

'''
2. Check if a character is a consonant
Input: "b"
Expected Output: Consonant
'''    
char = input("Enter a character: ")

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

if char.isalpha() and len(char) == 1:
    if char not in vowels:
        print("Consonant")
    else:
        print("Vowel")
else:
    print("Invalid input. Please enter a single alphabet character.")


'''
3. Check if a number is divisible by 2 or 3 but not both
Input: 6
Expected Output: Divisible by both 2 and 3
Input: 4
Output: Divisible by 2 only
'''
n = int(input("Enter a number: "))

if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2 only")
elif n % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 2 or 3")

'''
4. Check if a number is negative and odd
Input: -5
Expected Output: Negative and odd number
'''
n = int(input("Enter a number: "))

if n < 0 and n % 2 != 0:
    print("Negative and odd number")
else:
    print("Not Negative and odd number")

'''
5. Check if a string starts with a vowel
Input: "apple"
Output: Starts with a vowel
'''
char = input("Enter a string: ")
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

if char[0] in vowels:
    print("Starts with a vowel")
else:
    print("Does not start with a vowel")

'''
6. Check if three sides form a valid triangle
Input: 3, 4, 5
Output: Valid triangle
'''
#In any triangle, the sum of the lengths of any two sides must be greater than the length of the remaining side.
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")

'''
7. Find the greatest among three numbers
Input: 12, 45, 30
Output: 45 is the greatest
'''
a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
c = int(input("Enter num 3: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print(f"{a} is greatest")
elif b >= a and b >= c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")

'''
8. Check if a year is a century year and leap year
Input: 2000
Output: Century leap year
'''
year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Century leap year")
    else:
        print("Century non-leap year")
        
else:
    if year % 4 == 0:
        print("Non-century leap year")
    else:
        print("Non-century non-leap year")

'''
9. Check if a character is a digit
Input: "5"
Output: Digit
'''        
n = input("Enter a char: ")
if n.isdigit():
    print("Digit")
else:
    print("Not digit")

'''
10. Check if a number is palindrome (integer)
Input: 121
Output: Palindrome number
'''
n = int(input("Enter a number: "))

rev = int(str(n)[::-1])

if n == rev:
    print("Palindrome number")
else:
    print("Not palindrome")


'''
11. Compare lengths of two strings
Input: "cat", "mouse"
Output: Second string is longer
'''
n1 = input("Enter string1: ")
n2 = input("Enter string2: ")

if len(n1) > len(n2):
    print("First string is longer")
elif len(n1) == len(n2):
    print("Both strings are equal in length")
else:
    print("Second string is longer")

'''
12. Check if a number is within a specific range (50 to 100) and divisible by 5
Input: 75
Output: In range and divisible by 5
'''
n = int(input("Enter a number: "))

if n >= 50 and n <= 100 and n % 5 == 0:
    print("In range and divisible by 5")
else:
    print("Not in range or not divisible by 5")

'''
13. Validate if a password length is strong (8 or more characters)
Input: "secure123"
Output: Strong password
'''
n = input("Enter the password: ")

if len(n) >= 8:
    print("Strong password")
else:
    print("Weak password")


'''
14. Check if sum of two numbers is even
Input: 12, 16
Output: Sum is even
'''
n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))

if (n1 + n2) % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")

'''
15. Check if the character is a special symbol (!, @, #, etc.)
Input: "@"
Output: Special character
'''
n = input("Enter a char: ")

if not n.isalnum():
    print("Special character")
else:
    print("Not a special character")

'''
16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)
Input: 10
Output: Cold
'''
temp = int(input("Enter the temperature in °C: "))

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")

'''
17. Check if a number lies outside the range 10 to 50
Input: 55
Output: Outside the range
'''
n = int(input("Enter a number: "))

if n < 10 or n > 50:
    print("Outside the range")
else:
    print("Within the range")

'''
18. Check if number is a perfect square (basic method)
Input: 36
Output: Perfect square
'''
n = int(input("Enter a number: "))

# Check if square root is an integer
if int(n ** 0.5) ** 2 == n:
    print("Perfect square")
else:
    print("Not a perfect square")

'''
19. Compare two ages and determine who is older or if same age
Input: 22, 25
Output: Second person is older
'''
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))

if age1 > age2:
    print("First person is older")
elif age1 < age2:
    print("Second person is older")
else:
    print("Both are of the same age")

'''
20. Check if an angle is acute, right, or obtuse
Input: 90
Output: Right angle
'''
angle = int(input("Enter the angle in degrees: "))

if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")





