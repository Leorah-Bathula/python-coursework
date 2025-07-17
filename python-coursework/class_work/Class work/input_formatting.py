''' Input Formatting
Python's input() function is used to take input from the user during program execution. By
default, it returns a string. We often convert the input into int, float, list, tuple, set,
or dict as needed. '''

# 1. String Input --> Use case: Entering a name, email, city, etc.
name = input("Enter your full name: ")
print(name)

# 2. Integer Input --> Use case: Age, quantity, mobile number, number of items in cart.
quantity = int(input("Enter the number of items: "))
print(quantity)

# 3. Float Input --> Use case: Price, temperature, discount, rating.
price = float(input("Enter the product price: "))
print(price)

# 4. Input as List (Space-separated) --> Use case: List of names, marks, or product IDs.
names = input("Enter employee names (space-separated): ").split()
print(names)

# 5. Input as List (Comma-separated) --> Use case: Tags, emails, product categories.
tags = input("Enter tags (comma-separated): ").split(",")
print(tags)

# 6. List of Integers --> Use case: Marks, product prices, IDs.
marks = list(map(int,input("Enter marks: ").split()))
print(marks)

# 7. List of Floats --> Use case: Sensor readings, weights, product prices.
weights = list(map(float,input("Enter weights: ").split()))
print(weights)

# 8. Tuple Input --> Use case: Coordinates, dimensions (length, width, height).
dimensions = tuple(map(int, input("Enter length, width , height: ").split()))
print(dimensions)

# 9. Set Input --> Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharing app).
selected_ids = set(map(int,input("Enter selected image IDs: ").split()))
print(selected_ids)

# 10. Dictionary Input using eval() ---> Use case: When entering structured data like configuration settings or user profiles.
profile = eval(input("Enter user profile as a dictionary: "))
print(profile)

# 11. Multiple Inputs with Unpacking --> Use case: Login form or payment details.
username , password = input("Enter username and password: ").split()
print("Username:",username)
print("Password:",password)
