# print(object, ..sep = " ", end = '\n', file = sys.stdout , flush = False)

# Examples of print statements
print("Hello , World!")

name = "Leorah"
age =  21
print("Name:", name, "Age:", age)

#using separator 
print("2023","02","07", sep = "-")

# d) Using end to Control Line Endings
print("Hello, ", end = " ")
print("World")
#Here, end=" " prevents the default new line, and the second print() continues on the same line.

# Printing Special Characters
# New line (\n)
# Tab (\t)

print("Line 1\nLine 2")
print("Name:\tAlice")

#Using Modulo Operator (% Formatting)
name = "Jes"
age = 21
score = 98.75

# using modulo operator
print("Name: %s | Age: %d | Score: %.2f" % (name,age,score))

# Using f-strings (Formatted String Literals)
name = "Jes"
age = 21
score = 98.75
print(f"name: {name} | age: {age} | score: {score:.2f} ")
print("name: {} | age: {} | score: {:.1f}".format(name,age,score))

# {} → Placeholder for variables.
# {:.1f} → Formats the score with 1 decimal place.

