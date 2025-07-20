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



