
# 1.Arithemetic operators 
a = 50 
b =  30 
print('Addition of (a+b):' , a + b)
print("Multiplication of (a * b): ", a * b)
print("Subtraction of (a -b): " , a - b)
print("Division of (a / b): ", a / b)
print("Floor Division of (a // b): ", a//b)
print("Exponential of (a ** b): ", a ** b)


# 2.Assignment operators 
x = 5 # = symbol assigns a value to a variable 
x += 7 # same as x = x + 7
print("Add & Assign",x)
x -= 2 
print("Subtract & Assign",x)
x *= 4 
print("Multiply & Assign",x)
x /= 2
print("Divide & Assign",x)
x //= 3 
print("Floor Divide & Assign",x)
x %= 2
print("Modulus & Assign",x)
x **= 3
print("Exponentiate & Assign",x)

# 3.Logical Operators 
x = 2
y = 10 
print(x > 5 and y < 15) # Returns True if both conditions are true
print(x < 5 or y > 15) # Returns True if atleast one condition is true
print(not (x > 5)) # Reverses the condition(True becomes False)

# 4.Comparision Operators
x = 10
y = 5
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: True
print(x < y) # Output: False
print(x >= 10) # Output: True
print(y <= 5) # Output: True



# 5.Membership Operators 
# Checks if a value exists in a sequence 
# in (Returns True if the value exists in the sequence)
# not in (Returns True if the value does NOT exist in the sequence) 

s = {4,3,21,89}
print(1 in s)
print(4 in s)
print(22 not in s)

d = {'Name': 'Leorah','Batch': 31, "Course":"Python"}
print("Name" in d,"Leorah")
print("Leorah" in d) # returns false as it is checking value, it return true for keys 

l = ["Chicago","USA","Texas"]
print("USA" in l, "USA")
print("USA" not in l, "USA")

t = ("Jake","Ben","Joy")
print("Leo" not in t,"Leo")
print("Jake" in t,"Jake")



# 6.Identity Operators (Checks whether two variables refer to the same object in memory)
# Declare a set
s = {1,2,3}
m  = {1,2,3}
print(id(s)) # To check the memory location number
print(id(m))
print(s is m) # Returns True if both refer to the same object
# Returns False in this case because the id's are different
# So assign n = m 
n = m
print(id(n)) # id of n and m will be same now
print(n is m) # Returns True in this case
print(n is s) # Returns False in this case
print(n is not s) # Returns True in this case

# 7. Bitwise Operators
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)
