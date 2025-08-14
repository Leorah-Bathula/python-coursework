# my_programs.py

def armstrong_number():
    print("🧠 Program: Armstrong Number")
    print("""\
def is_armstrong(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_powers
""")
    print("🧪 Test Case 1: is_armstrong(153) → True")
    print("🧪 Test Case 2: is_armstrong(9474) → True")
    print("📝 Explanation: An Armstrong number is equal to the sum of its digits "
          "raised to the power of the number of digits.")

def swap_numbers():
    print("🧠 Program: Swap Two Numbers")
    print("""\
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print("🧪 Test Case 1: swap(10, 20) → (20, 10)")
    print("🧪 Test Case 2: swap(-5, 3) → (3, -5)")
    print("📝 Explanation: Uses tuple unpacking to swap without a temporary variable.")

def count_vowels():
    print("🧠 Program: Count Vowels in a String")
    print("""\
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
""")
    print("🧪 Test Case 1: count_vowels('Hello') → 2")
    print("🧪 Test Case 2: count_vowels('Python') → 1")
    print("📝 Explanation: Checks each character against a vowel set and counts matches.")

def gcd_two_numbers():
    print("🧠 Program: GCD of Two Numbers")
    print("""\
import math
def gcd(a, b):
    return math.gcd(a, b)
""")
    print("🧪 Test Case 1: gcd(54, 24) → 6")
    print("🧪 Test Case 2: gcd(101, 103) → 1")
    print("📝 Explanation: Uses Python's built-in math.gcd() for greatest common divisor.")

def reverse_number():
    print("🧠 Program: Reverse a Number")
    print("""\
def reverse_number(n):
    return int(str(n)[::-1])
""")
    print("🧪 Test Case 1: reverse_number(1234) → 4321")
    print("🧪 Test Case 2: reverse_number(9070) → 709")
    print("📝 Explanation: Converts number to string, reverses, and converts back to int.")

def sum_of_digits():
    print("🧠 Program: Sum of Digits")
    print("""\
def sum_of_digits(n):
    return sum(int(d) for d in str(n))
""")
    print("🧪 Test Case 1: sum_of_digits(123) → 6")
    print("🧪 Test Case 2: sum_of_digits(987) → 24")
    print("📝 Explanation: Loops through digits as characters, converts to int, sums them.")

def count_words():
    print("🧠 Program: Count Words in a Sentence")
    print("""\
def count_words(sentence):
    return len(sentence.split())
""")
    print("🧪 Test Case 1: count_words('Hello World') → 2")
    print("🧪 Test Case 2: count_words('Python is fun') → 3")
    print("📝 Explanation: Splits sentence by spaces and counts resulting words.")

def title_case():
    print("🧠 Program: Convert String to Title Case")
    print("""\
def title_case(s):
    return s.title()
""")
    print("🧪 Test Case 1: title_case('hello world') → 'Hello World'")
    print("🧪 Test Case 2: title_case('python programming') → 'Python Programming'")
    print("📝 Explanation: Uses Python’s str.title() to capitalize each word.")

def palindrome_check():
    print("🧠 Program: Check Palindrome")
    print("""\
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
""")
    print("🧪 Test Case 1: is_palindrome('Madam') → True")
    print("🧪 Test Case 2: is_palindrome('Hello') → False")
    print("📝 Explanation: Compares string with its reverse after converting to lowercase.")

def factorial():
    print("🧠 Program: Factorial of a Number")
    print("""\
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
""")
    print("🧪 Test Case 1: factorial(5) → 120")
    print("🧪 Test Case 2: factorial(0) → 1")
    print("📝 Explanation: Multiplies numbers from 1 to n to get the factorial.")

def fibonacci():
    print("🧠 Program: Fibonacci Series up to n terms")
    print("""\
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
""")
    print("🧪 Test Case 1: fibonacci(5) → [0, 1, 1, 2, 3]")
    print("🧪 Test Case 2: fibonacci(7) → [0, 1, 1, 2, 3, 5, 8]")
    print("📝 Explanation: Each term is the sum of the two previous terms.")

def decimal_to_binary():
    print("🧠 Program: Convert Decimal to Binary")
    print("""\
def decimal_to_binary(n):
    return bin(n).replace('0b', '')
""")
    print("🧪 Test Case 1: decimal_to_binary(10) → '1010'")
    print("🧪 Test Case 2: decimal_to_binary(255) → '11111111'")
    print("📝 Explanation: Uses Python’s bin() function and removes '0b' prefix.")

def prime_check():
    print("🧠 Program: Check Prime Number")
    print("""\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
""")
    print("🧪 Test Case 1: is_prime(7) → True")
    print("🧪 Test Case 2: is_prime(10) → False")
    print("📝 Explanation: Checks divisibility up to square root of n.")

def custom_sort():
    print("🧠 Program: Custom Sorting (Descending)")
    print("""\
def custom_sort(lst):
    return sorted(lst, reverse=True)
""")
    print("🧪 Test Case 1: custom_sort([3,1,2]) → [3,2,1]")
    print("🧪 Test Case 2: custom_sort([10,5,7]) → [10,7,5]")
    print("📝 Explanation: Uses sorted() with reverse=True for descending order.")

def even_odd_check():
    print("🧠 Program: Check Even or Odd")
    print("""\
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
""")
    print("🧪 Test Case 1: even_or_odd(4) → 'Even'")
    print("🧪 Test Case 2: even_or_odd(7) → 'Odd'")
    print("📝 Explanation: Uses modulus to check if number is divisible by 2.")
