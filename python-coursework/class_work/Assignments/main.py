# main.py
import my_programs as mp

menu = [
    "Armstrong Number",
    "Swap Two Numbers",
    "Count Vowels in String",
    "GCD of Two Numbers",
    "Reverse a Number",
    "Sum of Digits",
    "Count Words in a Sentence",
    "Convert String to Title Case",
    "Palindrome Check",
    "Factorial of a Number",
    "Fibonacci Series",
    "Convert Decimal to Binary",
    "Prime Number Check",
    "Custom Sorting",
    "Check Even or Odd"
]

functions = [
    mp.armstrong_number,
    mp.swap_numbers,
    mp.count_vowels,
    mp.gcd_two_numbers,
    mp.reverse_number,
    mp.sum_of_digits,
    mp.count_words,
    mp.title_case,
    mp.palindrome_check,
    mp.factorial,
    mp.fibonacci,
    mp.decimal_to_binary,
    mp.prime_check,
    mp.custom_sort,
    mp.even_odd_check
]

while True:
    print("\n------ FUNCTION MENU ------")
    for i, name in enumerate(menu, 1):
        print(f"{i}. {name}")
    print("0. Exit")
    print("----------------------------")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting program. Goodbye!")
            break
        elif 1 <= choice <= 15:
            print("\n" + "="*50)
            functions[choice-1]()
            print("="*50)
        else:
            print("Invalid choice. Please enter between 0-15.")
    except ValueError:
        print("Please enter a valid number.")
