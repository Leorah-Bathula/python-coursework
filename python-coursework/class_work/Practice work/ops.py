''' # Class blueprint for creating objects 
# Defines the attributes(data) and methods(functions) that the objects will have 

# Step:1 Define the class
class Product:
    # Attributes (data)
    name = "Laptop"
    price = 50000
    quantity = 10

    #Methods (functions)
    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

# Step2: Create objects of the product class

product1 = Product()
product2 = Product()

product1.display_info()
product2.display_info()

# Step3: Modify attributes
product1.name = "Smartphone"
product1.price = 30000
product1.quantity = 5

product1.display_info()

# Types of attributes 
# 1. Instance attributes
# 2. Class Attributes

# 1. Instance attributes
# defined inside the __init_ constructor using self 
# unique for each instance of the class

class Product:
    def __init__(self,name,price,quantity):
        self.name = name # Instance attribute
        self.price = price
        self.quantity = quantity

p1 = Product("Laptop",40000,10)  
p2 = Product("Phone",20000,5) 

print(p1.name)
print(p2.name)
     

# 2. Class attribute
# shared among all instances of the class , defined outside __init__ and accesed using ClassName.attribute 

class Product:
    discount = 10 # Class attribute 

    def __init__(self,name,price):
        self.name = name 
        self.price = price

# Accessing class attribute '
print(Product.discount)         


# Methods 
# Methods are the functions that belong to a  class
# They define the behaviur of the object 

# Adding a method
# Step 4 : Add a method to calculate total price 

class Product:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity 

    def display_info(self):
        print(f"Prodcut: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def calculate_total_price(self):
        return self.price * self.quantity

# Create an object 
product1 = Product("Tablet",20000,3)
print("Total Price: ",product1.calculate_total_price())


# Types of methods
# 1.Instance Methods
# 2.Class Methods
# 3.Static Methods

# 1.Instance Methods
class Product:
    def __init__(self,name,price):
        self.name = name 
        self.price = price

    def apply_discount(self,discount):
        self.price -= self.price * (discount/100) 

p1 = Product("Laptop",50000) 
p1.apply_discount(10)  
print(p1.price)     


# 2.Class Methods 
# Use @classmethod decorator 
# Work with class attributes using cls

class Product:
    discount = 10 # class atttribute 

    @classmethod 
    def set_discount(cls,new_discount):
        cls.discount = new_discount # Modifies class attribute

Product.set_discount(15)       
print(Product.discount) 
    
# 3.Static Methods
# Use @staticmethod decorator
# Independent of both instance and class attributes
# Used for utilty functions 

class Product:
    @staticmethod
    def is_expensive(price):
        return price > 30000
    
print(Product.is_expensive(50000))    
print(Product.is_expensive(20000))'''

'''# Real world example of an E-commerce Product class with attributes and methods;

class Product:
    discount = 5 # Class Attribute (default discount for all products)

    def __init__(self,name,price,quantity):
        self.name = name # Instance attribute
        self.price = price
        self.quantity = quantity 

    def apply_discount(self):
        # Instance method: applies discount to price  
        self.price -= self.price * (self.discount/100)

    @classmethod
    def update_discount(cls,new_discount):
        # Class method: Updates discount for all products
        cls.discount = new_discount

    @staticmethod
    def is_available(quantity):
        # Static method: Checks if produuct is avaialble 
        return quantity > 0

# Creating product instances 
p1 = Product("Laptop",50000,10)
p2 = Product("Phone",20000,5)   

# Applying discount
p1.apply_discount()
print(p1.price)

# Updating disocunt for all products 
Product.update_discount(10)
p2.apply_discount()
print(p2.price)

# Checking product availabilty 
print(Product.is_available(p1.quantity))'''

'''# self is a reference to the current instance of a class
'''
# Why is self important? 
# -> Differentiaties instance attributes from local variables
# -> Allows each instance to have unique attribute values 
# > Enables method calls on individual objects

# 1. self in instance methods
# 2. self helps in modifying instance attributes
# 3. self is not a keyword 
'''

# 1. self in instance methods 
'''
# -> used to access instance attributes inside the class 
# -> every instance method must include self as the first parameter 

'''
class Product:
    def __init__(self,name,price):
        self.name = name #assigning instance attributes
        self.price = price 

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price}")

# Creating objects 
p1 = Product("Laptop",70000)  
p2 = Product("Phone",20000)  

# Calling instance method
p1.display_info()
p2.display_info()

# 2.self helps in modifying instance attributes
# we can update attributes for each object using self

class Product:
    def __init__(self,name,price):
        self.name = name 
        self.price = price

    def apply_discount(self,discount):
        self.price -= self.price * (discount/100)  # Modifying instance attribute

p1 = Product("Laptop",50000)
p1.apply_discount(10) # applying 10% discount

print(p1.price)

# 3.self is Not  a keyword 
# self is just a naming convention, you can use any other name, but it's not recommended.

# 4. self vs class attributes(cls)
# 1. self refers to instance attributes 
# 2. cls(used in @classmethod) refers to class attributes

class Product:
    discount = 5 # Class Attribute 

    def __init__(self,name,price):
        self.name = name
        self.price = price 

    def apply_discount(self):
        self.price -= self.price * (self.discount/100) # usese self.disount

    @classmethod 
    def set_discount(cls,new_discount):
        cls.discount = new_discount # updates class attribute 

# Updating class discount 
Product.set_discount(10)  

p1 = Product("laptop",700000)
p1.apply_discount()
print(p1.price)

# Constructors 
# A constructor is a special method (__init__) that is automatically called when an object is created.
# it is used to initilize the objects attributes

class Product:
    # Constructor
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}')

# Create an object 
product1 = Product("Headphones",1500,10)
product1.display_info()'''

# ENCAPSULATION
# Bundles data(attributes) and methods(functions) into a single class unit(class)
# Why Encapsulation?
# 1. Data security, 2. Code maintainabilty , 3.Controlled access, 4.Data integrity 

# Types of attributes in encapsulation
# 1. public
# 2. protected(_)
# 3. private(__)

# Public Attributes: Can be accessed and modified from anywhere in the program 
# Example of public attribute(username)

'''class User:
    def __init__(self,username):
        self.username = username # public attribute 

# Creating an object 
user1 = User("john_doe")

# Accesing public attribute 
print(user1.username)

# Modifying public attribute 
user1.username = "jes_leorah"
print(user1.username)

# USe public attributes when data does not need any security or validation

# Protected attributes are meant to be used within the class and subclassses but can still be accessed from outside if needed
# Example of protected attribute(_otp)

class User:
    def __init__(self,username,otp):
        self.username = username # Public attribute 
        self._otp = otp # protected attribute 

# creating an object 
user1 = User("Jesleo","12345")  

# Accesing protected attribute 
print(user1._otp)

# modifying the protected attribute 
user1._otp = "89764"
print(user1._otp)
# Use protected attributes when data should not be freely modified but still needs to be accessible in subclasses
# Using protected attributes in subclass

class Admin(User):
    def show_otp(self):
        return f"Admin can see OTP: {self._otp}"
    
admin1 = Admin("admin_user","99999")  
print(admin1.show_otp())  

# Private attributes: are accesible only within the class and cannot be accesesd from outside 
# Example of private attribute(__password)

class User:
    def __init__(self,username,password):
        self.username = username # public attribute
        self.__password = password  # private atribute

# creating an  onject 
user1 = User("Jessie","leo@12")

# trying to acces private attribute directly will cuase an error 
# print(user1.__password)
# AttributeError: 'User' object has no attribute '__password'
    
# USe private attributes when data must be completely hidden from outside access.
# ex: passwords,account balances or sensitive user information

# Accessing private attributes using Getter and Setter methods

class User:
    def __init__(self,username,password):
        self.username = username 
        self.__password = password 

        # Getter method to retrieve password 
    def get_password(self):
        return "******"  
    
    # setter method to update pasword with validation
    def set_password(self,new_password):
        if len(new_password) < 6:
            print("Erro: Passwrod must be atleast 6 characters long")
        else:
            self.__password = new_password
            print("Password updated succesfully")   

# creating user object 
user1 = User("Jessie","123jdcc")

# Accesing password securley 
print(user1.get_password())

# UPDATING PASSWORD SECURELY 
user1.set_password("123") # Output: Error: Password must be at least 6 characters long.
user1.set_password("newSecurePassword")'''

# 7. Complete encapsulation example(public,protected,private attributes)

class User:
    def __init__(self,username,password,otp):
        self.username = username # public attribute 
        self._otp = otp # protecetd attribute
        self.__password = password # private attribute

    # Getter for password 
    def get_password(self):
        return "******"
    
    # Setter for password 
    def set_password(self,new_password):
        if len(new_password) < 6:
            print("Error: password must be atleast 6 chacaters long")
        else:
            self.__password = new_password
            print("Password updated succesfully")

    # Getter for oTp 
    def get_otp(self):
        return self._otp
    
    # Setter for otp 
    def set_otp(self,new_otp):
        self._otp = new_otp 
        print("OTP updated successfully")

# Creating a user object 
user1 = User("jesleorah","leo123","575767")  

# Accessing and modifying the public attribute 
print(user1.username)
user1.username = "Leorah.B"
print(user1.username)

# Accessing protected attribute 
print(user1.get_otp())
user1.set_otp("3724682")
print(user1.get_otp())

# Accesing private atribute vis getter 
print(user1.get_password())

# Updating private attribute via setter 
user1.set_password("newpass123")
