# BASICS (10 QUESTIONS)

1.
class Book:
    def __init__(self,title,author,price):
        self.title = title 
        self.author = author 
        self.price = price 
        
    def display_info(self): # method
        print(f'Title: {self.title}, Author: {self.author}, Price: ${self.price}')

# Object creation and method call 
book1 = Book("Clean Code","Robert Martin",450)
book1.display_info()

# Title: Clean Code, Author: Robert Martin, Price: $450
        
2.
class Employee:
    def __init__(self,name,base_salary):
        self.name = name 
        self.base_salary = base_salary 
        
    def calculate_annual_salary(self):
        return self.base_salary * 12 
        
# Object creation 
emp = Employee("John",34000)
print("Annual Salary: ",emp.calculate_annual_salary())
# Annual Salary:  408000

3.
class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 
        
    def is_passed(self):
        avg = sum(self.marks)/len(self.marks)
        return avg >= 40 
        
# Object and method call 
s1 = Student("Priya",[45,56,60])
print("Passed: ",s1.is_passed())
# Passed:  True

4.
class BankAccount:
    def __init__(self,owner):
        self.owner = owner 
        self.balance = 0 
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount 
        else:
            print("Insufficient balance")
            
    def show_balance(self):
        print(f"Balance: {self.balance}")
        
# use case 
acc = BankAccount("Arjun")
acc.deposit(2000)
acc.withdraw(500)
acc.show_balance()
# Balance: 1500

5.
class Car:
    def __init__(self,make,model):
        self.make = make 
        self.model = model 
        self.odometer = 0 
        
    def drive(self,km):
        self.odometer += km
        
    def show_odometer(self):
        print(f"Odometer: {self.odometer} km")
        
# create object 
car1 = Car("Toyota","Innova")
car1.drive(120)
car1.drive(30)
car1.show_odometer()
# Odometer: 150 km

6.
class Movie:
    def __init__(self,title,genre,rating):
        self.title = title 
        self.genre = genre
        self.rating = rating 
        
    def is_family_friendly(self):
        return self.rating < 13
        
m1 = Movie("Finding Nemo","Animation",8)
print("Family Friendly: ",m1.is_family_friendly())
# Family Friendly:  True

7.
class Product:
    def __init__(self,name,price):
        self.name = name 
        self.price = price
        
    def apply_discount(self,percent):
        self.price -= self.price * (percent / 100)
        
    def show_price(self):
        print(f"Discounted Price: {self.price}")
        
p = Product("Laptop",40000)        
p.apply_discount(10)
p.show_price()
# Discounted Price: 36000.0

8.
class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius 
    
    def to_fahrenheit(self):
        return (self.celsius* 9/5) + 32
        
    def to_celsius(self,fahrenheit):
        return (fahrenheit - 32) * 5/9
        
temp = Temperature(25)   
print("Fahrenheit:", temp.to_fahrenheit())
print("Celsius from 98F:", temp.to_celsius(98))

# Fahrenheit: 77.0
# Celsius from 98F: 36.666666666666664

9.
class InventoryItem:
    def __init__(self,name,quantity):
        self.name = name 
        self.quantity = quantity
        
    def update_quantity(self,amount):
        self.quantity += amount
        
    def display(self):
        print(f"{self.name}: {self.quantity} in stock")
        
item = InventoryItem("Mouse",50)     
item.update_quantity(-5)
item.display()
# Mouse: 45 in stock

10.
class Order:
    def __init__(self,order_id,status = "Pending"):
        self.order_id = order_id 
        self.status = status 
        
    def update_status(self,new_status):
        self.status = new_status
        
    def show_status(self):
        print(f"Order {self.order_id} status: {self.status}")
        
o = Order("ORD123")        
o.update_status("Shipped")
o.show_status()
# Order ORD123 status: Shipped

# INHERITANCE (10 QUESTIOINS)

11.
class Vehicle:
    def __init__(self,brand):
        self.brand = brand 
        
    def start(self):
        print(f"{self.brand} vehicle started")
        
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model 
        
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        
car1 = Car("Toyota","Camry")    
car1.start()
car1.show_info()
# Toyota vehicle started
# Brand: Toyota, Model: Camry



