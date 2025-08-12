# A function is a block of resuable code that performs a specific task 
# Syntax of a user-defined function 
def function_name(parameters):
    # Block of code
    return result 
    
# Example 1: Function without paramters and return   
def greet():
    print("HEllo")
greet()

# Example 2: Function with parameters
def add(a,b):
    print("Sum is: ",a + b)
    
add(3,5)   

# Example 3: Function with return value 
def multiply(x,y):
    return x * y 
result = multiply(4,5)
print("Result:",result)

# Types of arguments 
# 1.Positional arguments - based on order add(2,3)
# 2. Keyword Argument - based on name add(a =2,b = 3)
# 3. Default Arguments - predefined values 
def greet(name="Guest"):
    print("Hello",name)
    
greet()
greet("Jessi")

# Variable-length arguments 
# *args - for any number of positional arguments 
def total(*nums):
    print(sum(nums))
total(1,2,3,4) 

# **kwargs - for any number of keyword arguments 
def show_details(**info):
    print(info)
show_details(name="Leorah",age= 21)

# Scope of Variables 
#Local Variable - Defined inside a function -> onnly used there
# Global variable - Defined outsided all functions -> accessible everywhere
x = 10 # Global
def func():
    x = 5 # Local
    print(x)
    
func() # 5
print(x) # 10 








